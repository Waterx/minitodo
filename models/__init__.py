import time
from mongoengine import *
import uuid
import json

connect('minitodo')


class Model():


    meta = {'allow_inheritance': True}

    '''得到这张表的所有项的所有属性'''

    @classmethod
    def getAll(cls):
        t_list = cls.objects()
        dict_all = []
        for l in t_list:
            td = {}
            for i in range(len(cls.__fields__)):
                # print('model getall', getattr(l, cls.__fields__[i]))
                td[cls.__fields__[i]] = l[cls.__fields__[i]]
            # td = {'todo_id': l.todo_id,
            #       'title': l.title,
            #       'done':l.done,
            #       'dead_line':l.dead_line}
            dict_all.append(td)
        return json.dumps(dict_all)

    @classmethod
    def get_one_by(cls, **kwargs):
        t = None
        # print('meixingxing', kwargs)   这句不报错 {'todo_id': '6afbd6a4-5460-11e9-9c95-086266b4c7ac'}
        # print('youxingxing', **kwargs) 这句会报错
        # for a in kwargs:
        #     print(a, kwargs[a])
        for o in cls.objects(**kwargs):
            t = o
            break
        return t

    @classmethod
    def get_all_by(cls, **kwargs):
        t = None
        pass