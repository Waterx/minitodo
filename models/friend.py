import time
from mongoengine import *
import uuid
import json
from models import Model
from models.user import User
from models.group import Group

class Friend(Document, Model):
    __fields__ = [
        'user1',
        'user2'
    ]

    user1 = ReferenceField(User)
    user2 = ReferenceField(User)
    #
    # @classmethod
    # def add(cls, form, u1, u2):
    #     t = Note(
    #         user=u,
    #         group=g
    #     )
    #     t.save()
    #     print('model Note insert', t.title)
    #     d = dict(
    #         title=t.title,
    #         note_id=t.note_id,
    #         updated_time=t.updated_time,
    #     )
    #     return json.dumps(d)