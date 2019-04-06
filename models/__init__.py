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
            # len(cls.__fields__)有多少个属性项
            for i in range(len(cls.__fields__)):
                # print('model getall', getattr(l, cls.__fields__[i]))
                # 如果这个属性是一个类，判断
                flag = isinstance(l[cls.__fields__[i]], Model)
                if flag is False:
                    td[cls.__fields__[i]] = l[cls.__fields__[i]]
                elif flag is True:
                    if cls.__fields__[i] == 'project':
                        td[cls.__fields__[i]] = l[cls.__fields__[i]].project_id

            # td = {'todo_id': l.todo_id,
            #       'title': l.title,
            #       'done':l.done,
            #       'dead_line':l.dead_line}
            dict_all.append(td)
        print("!!Model dict_all", dict_all)

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
