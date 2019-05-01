import time
from mongoengine import *
import uuid
import json
from models import Model

class Project(Document, Model):

    __fields__ = [
        'project_id',
        'title',
        'done',
        'intro',
        'updated_time',
        # 'user'
    ]

    project_id = StringField(required=True)
    title = StringField(max_length=20)
    done = BooleanField(default=False)
    intro = StringField(max_length=50)
    updated_time = IntField()

    @classmethod
    def inserProject(cls, form):
        t = Project(
            title=form.get('title', ''),
            intro=form.get('intro', ''),
            done=False,
            project_id=str(uuid.uuid1()),
            updated_time=int(time.time())
        )
        t.save()
        print('model project insert', t.title, t.intro)
        d = dict(
            title=t.title,
            intro=t.intro,
        )
        return json.dumps(d)


    @classmethod
    def delProject(cls, form):
        pid = form['project_id']
        flag = Project.objects(project_id=pid).delete()
        print('model project', 'delProject', flag)
        if flag != 1:
            return 'wrong delete'
        return json.dumps(flag)
