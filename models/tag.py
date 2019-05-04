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
            tag_id = t.tag_id,
        )
        return json.dumps(d)

    @classmethod
    def delTag(cls, j):
        tagid = j['tag_id']
        flag = Tag.objects(tag_id=tagid).delete()
        print('model tag', 'delTag', flag)
        if flag != 1:
            return 'wrong delete'
        return json.dumps(flag)
