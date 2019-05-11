import time
from mongoengine import *
import uuid
import json
from models import Model
from models.user import User


class Group(Document, Model):
    __fields__ = [
        'group_id',
        'name',
        'icon',
        'intro',
        'updated_time',
        'admin',
        'users',

    ]

    group_id = StringField(required=True)
    name = StringField(max_length=20)
    intro = StringField(max_length=50)
    updated_time = IntField()
    admin = ReferenceField(User)
    user = ReferenceField(User)
    icon = StringField(max_length=50)
    users = ListField(ReferenceField(User, reverse_delete_rule=PULL))

    @classmethod
    def addGroup(cls, form, u):
        t = Group(
            name=form.get('name', ''),
            intro=form.get('intro', ''),
            group_id=str(uuid.uuid1()),
            updated_time=int(time.time()),
            icon='/static/images/clock.gif',
            admin=u,
            user=u,
        )
        userlist = [u]
        t.users = userlist
        t.save()
        print('model Group add', t.name)
        d = dict(
            name=t.name,
            group_id=t.group_id,
            intro=t.intro,
            admin=t.admin.user_id,
            icon=t.icon,
        )
        return json.dumps(d)

    @classmethod
    def participateGroup(cls, form, u):
        gid = form.get('group_id', '')
        print("model group participate gid", gid)
        g = Group.get_one_by(group_id=gid)
        if u not in g.users:
            g.users.append(u)
        else:
            print('用户已存在于群组')
        g.save()
        print("model group userlist", g.users)
        return ''


    @classmethod
    def getpall(cls, u):
        t_list = Group.objects(users__all=[u])
        print(list)
        dict_all = []
        for l in t_list:
            td = {}
            # len(cls.__fields__)有多少个属性项
            for i in range(len(cls.__fields__)):
                # 如果这个属性是一个类，判断
                flag1 = isinstance(l[cls.__fields__[i]], Model)
                if flag1 is False:
                    td[cls.__fields__[i]] = l[cls.__fields__[i]]

                if cls.__fields__[i] == 'users':
                    td[cls.__fields__[i]] = [a.icon for a in l[cls.__fields__[i]]]
                if cls.__fields__[i] == 'admin':
                    td[cls.__fields__[i]] = l[cls.__fields__[i]].name
            # td = {'todo_id': l.todo_id,
            #       'title': l.title,
            #       'done':l.done,
            #       'dead_line':l.dead_line}
            dict_all.append(td)
        print("!!Model getpall", dict_all)

        return json.dumps(dict_all)

