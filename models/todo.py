import time
from mongoengine import *
import uuid
import json

connect('minitodo')


class Todo(Document):

    __fields__ = [
        'todo_id',
        'title',
        'done',
        'dead_line',
        'rank',
    ]

    todo_id = StringField(required=True)
    title = StringField(max_length=30)
    done = BooleanField(default=False)
    dead_line = StringField(max_length=30)
    rank = StringField(max_length=1)

    # user_id = StringField(default='123')

    # @classmethod
    # def get(cls, id):
    #     m = cls.find_by(id=id)
    #     m.views += 1
    #     m.save()
    #     return m

    @classmethod
    def getAll(cls):
        list = Todo.objects()
        dict_all=[]
        for l in list:
            td = {}
            for i in range(len(Todo.__fields__)):
                print(getattr(l, Todo.__fields__[i]))
                td[Todo.__fields__[i]] = l[Todo.__fields__[i]]
            # td = {'todo_id': l.todo_id,
            #       'title': l.title,
            #       'done':l.done,
            #       'dead_line':l.dead_line}
            dict_all.append(td)
        return json.dumps(dict_all)

    @classmethod
    def inserTodo(cls, form):
        t = Todo(
            title=form.get('title', ''),
            done=False,
            todo_id=str(uuid.uuid1())
        )
        t.save()

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
        print('model toggletodo', 'tid',tid)
        for todo in Todo.objects(todo_id=tid):
            t = todo
            break
        if t is None:
            return 'wrong id'
        td = t.done

        t.done = not td
        t.save()
        result = json.dumps(t.todo_id)
        return result

    @classmethod
    def editTodo(cls, form):
        tid = form['todo_id']
        ttitle = form['title']
        print('!!edit', tid, ttitle)
        t = None
        for todo in Todo.objects(todo_id=tid):
            t = todo
            break
        print(t)
        t.title = ttitle
        t.save()
        result = json.dumps(t.todo_id)
        return result


    def todoDict(self):
        return {
            'title': self.title,
            'todo_id': self.todo_id,
            'done': self.done
        }
class Todox():
    def __init__(self, form):
        title = form.title
        done = form.done


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

print(Todo.getAll())