import time
from mongoengine import *
import uuid

connect('minitodo')


class Todo(Document):
    todo_id = StringField(required=True)
    title = StringField(max_length=50)
    done = BooleanField(default=False)
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
            td = {'todo_id': l.todo_id,
                  'title': l.title,
                  'done':l.done}
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


list = Todo.objects()
for l in list:

    print(type(l), l.done, l.title)

class User():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

u1 = User('laohe',40)
print(u1.__dict__)
import json
print(json.dumps(Todo.getAll()))
# for post in Todo.objects(done=False):
#     print(post.title)
