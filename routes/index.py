from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
    send_from_directory,
)

from models.todo import Todo
from models.user import User
from utils import log
import json
main = Blueprint('index', __name__)


def current_user():
    # 从 session 中找到 user_id 字段, 找不到就 -1
    # 然后 User.find_by 来用 id 找用户
    # 找不到就返回 None
    uid = session.get('user_id', -1)
    if uid==-1:
        print('当前用户不存在')
        return None
    u = User.get_one_by(user_id=uid)
    print('当前用户：', u.email)
    return u


"""
用户在这里可以
    访问首页
    注册
    登录

用户登录后, 会写入 session
"""


@main.route("/")
def index():
    u = current_user()
    if u is not None:
        # 若有用户
        return render_template("index.html", user=u)
    else:
        return render_template("login.html", user=u)

@main.route("/register", methods=['POST'])
def register():
    form = request.form
    # 用类函数来判断
    u = User.register(form)
    print('route index u.email', u.email)
    return redirect(url_for('.index'))


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)

    if u is None:
        # 转到 topic.index 页面
        print('没有这个用户')
        return redirect(url_for('.index'))
    else:
        print('route index login u', u.email)
        print('有这个用户')
        # session 中写入 user_id
        session['user_id'] = u.user_id
        print('写入session', session['user_id'])
        # 设置 cookie 有效期为 永久
        session.permanent = True
        return redirect(url_for('.index'))


@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!add form', form)
    # ImmutableMultiDict([('title', '的撒发射点法大师傅大师傅')])
    u = current_user()
    # u代表user
    t = Todo.inserTodo(form, u)
    return redirect(url_for('.index'))


@main.route("/all")
def all():
    u = current_user()
    t_list = Todo.getAll(u)
    return (t_list)

@main.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    print('!!delete json', json['todo_id'])
    result_status = Todo.delTodo(json)
    return result_status

@main.route("/check", methods=['POST'])
def check():
    json = request.get_json()
    ''' 返回数据如
        {'todo_id': '42d9ea70-4248-11e9-a247-40e230d295fe'}
    '''
    # 客户端用ajax请求时一般传过来的是json字符串，用get_json解析，返回的
    # 时候也要转成json字符串传回去
    print('!!check json', json)
    result_id = Todo.toggleTodo(json)
    return result_id

@main.route("/edit", methods=['POST'])
def edit():
    json = request.get_json()
    print('!!edit json', json)
    result_id = Todo.editTodo(json)
    return result_id

@main.route("/reorder", methods=['POST'])
def reorder():
    form = request.form
    print('!!reorder form', form)
    result_id = Todo.reorderTodo(form)
    return redirect(url_for('.index'))
