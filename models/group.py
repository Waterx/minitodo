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
