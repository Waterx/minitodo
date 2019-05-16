import time
from mongoengine import *
import uuid
import json
from models import Model
from models.user import User
from models.group import Group

class Note(Document, Model):
    __fields__ = [
        'note_id',
        'title',
        'updated_time',
        'user',
        'group'
    ]

    note_id = StringField(required=True)
    title = StringField(max_length=70)
    updated_time = IntField()
    user = ReferenceField(User)
    group = ReferenceField(Group)

    @classmethod
    def inserNote(cls, form, u, g):
        t = Note(
            title=form.get('title', ''),
            note_id=str(uuid.uuid1()),
            updated_time=int(time.time()),
            user=u,
            group=g
        )
        t.save()
        print('model Note insert', t.title)
        d = dict(
            title=t.title,
            note_id=t.note_id,
            updated_time=t.updated_time,
        )
        return json.dumps(d)

    @classmethod
    def delNote(cls, j):
        noteid = j['note_id']
        # ??????????
        flag = Note.objects(note_id=noteid).delete()
        print('model note', 'delNote', flag)
        if flag != 1:
            return 'wrong delete'
        return json.dumps(flag)