import time
from mongoengine import *
import uuid
import json
from models import Model
from models.user import User

class Note(Document, Model):
    __fields__ = [
        'note_id',
        'title',
        'updated_time',
        'user'
    ]

    note_id = StringField(required=True)
    title = StringField(max_length=40)
    updated_time = IntField()
    user = ReferenceField(User)

    @classmethod
    def inserNote(cls, form, u):
        t = Note(
            title=form.get('title', ''),
            note_id=str(uuid.uuid1()),
            updated_time=int(time.time()),
            user=u
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