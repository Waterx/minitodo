import time
from mongoengine import *
import uuid
import json
from models import Model
from models.user import User
from models.group import Group

class Chat(Document, Model):
    __fields__ = [
        'chat_id',
        'title',
        'updated_time',
        'userfrom',
        'userto'
        'group',
        'readed'
    ]

    chat_id = StringField(required=True)
    title = StringField(max_length=70)
    updated_time = IntField()
    userfrom = ReferenceField(User)
    userto = ReferenceField(User)
    group = ReferenceField(Group)
    readed = BooleanField(default=False)
    @classmethod
    def getAllc(cls, u):

        pass
    @classmethod
    def add(cls, j, userfrom, userto):
        u1 = User.get_one_by(user_id=userfrom)
        u2 = User.get_one_by(user_id=userto)

        t = Chat(
            title=j.get('title', ''),
            chat_id=str(uuid.uuid1()),
            updated_time=int(time.time()),
            userfrom=u1,
            userto=u2,
            readed = False
        )
        t.save()
        d = dict(
            chat_id = t.chat_id,
            updated_time=t.updated_time,
            title = t.title,
            userfromicon=u1.icon,
            usertoicon=u2.icon
        )
        return json.dumps(d)

    @classmethod
    def chatall(cls, u1, u2, rtime):
        u1 = User.get_one_by(user_id=u1)
        u2 = User.get_one_by(user_id=u2)
        if rtime is None:
            list1 = Chat.objects(userfrom=u1, userto=u2)
            list2 = Chat.objects(userto=u1, userfrom=u2)
        else:
            list1 = Chat.objects(userfrom=u1, userto=u2, updated_time__gt=rtime)
            list2 = Chat.objects(userto=u1, userfrom=u2, updated_time__gt=rtime)
            # list2 = []
        list = []

        for l in list1:
            td = {
                'updated_time': l.updated_time,
                'title': l.title,
                'userfrom': l.userfrom.name,
                'userto': l.userto.name,
                'userfromicon':l.userfrom.icon,
                'usertoicon': l.userto.icon

            }
            list.append(td)

        for l in list2:
            td = {
                'updated_time': l.updated_time,
                'title': l.title,
                'userfrom': l.userfrom.name,
                'userto': l.userto.name,
                'userfromicon': l.userfrom.icon,
                'usertoicon': l.userto.icon
            }
            list.append(td)

        def taket(c):
            return c['updated_time']
        list.sort(key=taket)
        print(list)
        return json.dumps(list)


    @classmethod
    def changereaded(cls, cid):
        c = Chat.get_one_by(chat_id=cid)
        c.readed = True
        c.save()
        return json.dumps(cid)