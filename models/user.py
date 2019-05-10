import time
from mongoengine import *
import uuid
import json
from models import Model


class User(Document, Model):
    __fields__ = [
        'user_id',
        'name',
        'email',  # email来当登陆账号使用
        'password'
        'updated_time',
        'icon',

        # 'user'
    ]

    user_id = StringField(required=True)
    name = StringField(max_length=20)
    email = StringField(required=True, max_length=30)
    password = StringField(required=True, max_length=100)
    icon = StringField(max_length=100)
    updated_time = IntField()


    def salted_password(pwd):
        salt = '$!@><?>HUI&DWQa`'
        import hashlib
        def sha256(ascii_str):
            return hashlib.sha256(ascii_str.encode('ascii')).hexdigest()

        hash1 = sha256(pwd)
        hash2 = sha256(hash1 + salt)
        hash2 = hash2[:64]
        return hash2

    # @classmethod
    # def addUser(cls, form):
    #     t = User(
    #         name=form.get('name', ''),
    #         email=form.get('email', ''),
    #         user_id=str(uuid.uuid1()),
    #         updated_time=int(time.time()),
    #         password=cls.salted_password(form.get('password', '')),
    #         icon='/static/images/default.png'
    #     )
    #     t.save()
    #     print('model User insert', t.email)
    #     d = dict(
    #         title=t.name,
    #         email=t.email,
    #         user_id=t.user_id,
    #         icon=t.icon,
    #     )
    #     return json.dumps(d)

    @classmethod
    def register(cls, form):
        email = form.get('email', '')
        pwd = form.get('password', '')
        name = form.get('name', 'aaa')
        print('modal user email', email)
        print('modal user email', name)

        if len(email) > 2 and User.get_one_by(email=email) is None:
            t = User(
                name=name,
                email=email,
                user_id=str(uuid.uuid1()),
                updated_time=int(time.time()),
                icon='/static/images/cat.jpg',
                password=User.salted_password(pwd)
            )
            t.save()
            return t
        else:
            return None

    @classmethod
    def validate_login(cls, form):
        user = User.get_one_by(email=form['email'])
        if user is not None and user.password == User.salted_password(form['password']):
            return user
        else:
            return None
