import time
from mongoengine import *
import uuid
import json
from models import Model

class Tag(Document, Model):

    __fields__ = [
        'tag_id',
        'title',
        'updated_time',
        # 'user'
    ]

    tag_id = StringField(required=True)
    title = StringField(max_length=20)
    updated_time = IntField()

    @classmethod
    def inserTag(cls, form):
        t = Tag(
            title=form.get('title', ''),
            tag_id=str(uuid.uuid1()),
            updated_time=int(time.time())
        )
        t.save()
        print('model Tag insert', t.title)
        d = dict(
            title=t.title,
        )
        return json.dumps(d)