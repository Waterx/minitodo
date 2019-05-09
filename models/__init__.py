import time
from mongoengine import *
import uuid
import json

connect('minitodo')


class Model():
    meta = {'allow_inheritance': True}

    '''得到这张表的所有项的所有属性'''

    @classmethod
    def getAll(cls, u):
        t_list = cls.objects(user=u)
        dict_all = []
        for l in t_list:
            td = {}
            # len(cls.__fields__)有多少个属性项
            for i in range(len(cls.__fields__)):
                # 如果这个属性是一个类，判断
                flag1 = isinstance(l[cls.__fields__[i]], Model)
                flag2 = isinstance(l[cls.__fields__[i]], list)
                if flag1 is False:
                    td[cls.__fields__[i]] = l[cls.__fields__[i]]
                elif flag1 is True:
                    if cls.__fields__[i] == 'project':
                        # l[cls.__fields__[i]]是一个Project object
                        td[cls.__fields__[i]] = l[cls.__fields__[i]].project_id

                if cls.__fields__[i] == 'tag':
                    td[cls.__fields__[i]] = [a.tag_id for a in l[cls.__fields__[i]]]

                        # print('!!!!!!', [l[cls.__fields__[i]].tag_id for a in l[cls.__fields__[i]]])
                        # td[cls.__fields__[i]]=''
                        #

            # td = {'todo_id': l.todo_id,
            #       'title': l.title,
            #       'done':l.done,
            #       'dead_line':l.dead_line}
            dict_all.append(td)
        print("!!Model dict_all", dict_all)

        return json.dumps(dict_all)
        # return '1'

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
        t = cls.objects(**kwargs)
        return t
