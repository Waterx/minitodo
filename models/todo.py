import time
from mongoengine import *
import uuid
import json
from models import Model
from models.project import Project
from models.tag import Tag

class Todo(Document, Model):

    '''
    凡是写在fields里面的都是可以公开访问的
    '''
    __fields__ = [
        'todo_id',
        'title',
        'done',
        'dead_line',
        'rank',
        'updated_time',
        'project',
        'tag',
        # 'user'

    ]

    todo_id = StringField(required=True)
    title = StringField(max_length=20)
    done = BooleanField(default=False)
    dead_line = StringField(max_length=30)
    rank = StringField(max_length=1)
    updated_time = IntField()
    project = ReferenceField(Project)
    tag = ListField(ReferenceField(Tag))
    # user = ReferenceField()

    # user_id = StringField(default='123')

    # @classmethod
    # def get(cls, id):
    #     m = cls.find_by(id=id)
    #     m.views += 1
    #     m.save()
    #     return m

    @classmethod
    def inserTodo(cls, form):
        t = Todo(
            title=form.get('title', ''),
            done=False,
            todo_id=str(uuid.uuid1()),
            rank=form.get('rank', 3),
            updated_time=int(time.time())
        )
        t.save()

    @classmethod
    def reorderTodo(cls, form):
        tid = form.get('todo_id', '')
        print('!!model reorder', tid)
        t = Todo.get_one_by(todo_id=tid)
        t.dead_line = form.get('dead_line', '')
        print('!!model reorder', t.dead_line)
        t.rank = form.get('rank', 3)
        print('!!model reorder', t.rank)
        pid = form.get('project')
        t.project = Project.get_one_by(project_id=pid)

        # 注意getlist可以得到重复的键对应的值并生成列表
        print('!!model reorder tag', form.getlist('tag'))
        tagidlist = form.getlist('tag')
        taglist = []
        # 这里有个命名的坑已解决
        for i in tagidlist:
            tag = Tag.get_one_by(tag_id=i)
            taglist.append(tag)
        print(taglist)
        t.tag = taglist
        t.save()
        return tid

    '''
        该函数作用是通过todo_id删除todo，返回todo_id的字符串
        注意，这里的form实际上是一个json串
    '''

    @classmethod
    def delTodo(cls, form):
        tid = form['todo_id']
        print(tid)
        flag = Todo.objects(todo_id=tid).delete()
        print('model todo', 'delTodo', flag)
        if flag != 1:
            return 'wrong delete'
        return json.dumps(flag)


    '''
        该函数作用是改变todo的done值，返回todo_id的字符串
        注意，这里的form实际上是一个json串
    '''
    @classmethod
    def toggleTodo(cls, form):
        t = None
        tid = form['todo_id']
        print('model toggletodo', 'tid', tid)
        t = Todo.get_one_by(todo_id=tid)
        td = t.done
        t.done = not td
        t.save()
        result = json.dumps(t.todo_id)
        return result

    @classmethod
    def editTodo(cls, form):
        tid = form['todo_id']
        t_title = form['title']
        print('!!edit', tid, t_title)
        t = Todo.get_one_by(todo_id=tid)
        t.title = t_title
        t.save()
        result = json.dumps(t.todo_id)
        return result

    @classmethod
    def delTodobyProject(cls, pid):
        project = None
        for p in Project.objects(project_id=pid):
            project = p
            break
        Todo.objects(project=project).delete()

    @classmethod
    def getTodobyProject(cls, pid):
        list = []
        project = None
        project = Project.get_one_by(project_id=pid)
        for t in Todo.objects(project=project):
            dic = {
                'todo_id': t.todo_id,
                'title': t.title,
                'done': t.done,
                'dead_line': t.dead_line,
                'updated_time': t.updated_time,
            }
            list.append(dic)
        print('!!model todo gettodobyproj list', list)
        return json.dumps(list)






# t1 = Todo(
#     title='李白',
#     done = True,
#     todo_id = str(uuid.uuid1())
# )
# t2 = Todo(
#     title='杜甫daf',
#     done = True,
#     todo_id = str(uuid.uuid1())
# )
# t3 = Todo(
#     title='ddd李商隐ddddd',
#     done = False,
#     todo_id = str(uuid.uuid1())
# )
# t1.save()
# t2.save()
# t3.save()

# for post in Todo.objects:
#     print(post.title)
# sdaf
# saaaaadaf
# dddddddd

#
# list = Todo.objects()
# for l in list:
#     print(type(l), l.done, l.title)
'''
    class User():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    u1 = User('laohe',40)
    print(u1.__dict__)
'''

# import json
# print(json.dumps(Todo.getAll()))

# for post in Todo.objects(done=False):
#     print(post.title)

# Todo.delTodo({'todo_id': 'dd348eb4-43aa-11e9-8ca5-40e230d295fe'})
