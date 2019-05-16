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
        return json.dumps(t.chat_id)
    @classmethod
    def changereaded(cls, cid):
        c = Chat.get_one_by(chat_id=cid)
        c.readed = True
        c.save()
        return json.dumps(cid)