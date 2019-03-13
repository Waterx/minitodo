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
from utils import log
main = Blueprint('index', __name__)


# def current_user():
#     # 从 session 中找到 user_id 字段, 找不到就 -1
#     # 然后 User.find_by 来用 id 找用户
#     # 找不到就返回 None
#     uid = session.get('user_id', -1)
#     u = User.find_by(id=uid)
#     return u


"""
用户在这里可以
    访问首页
    注册
    登录

用户登录后, 会写入 session, 并且定向到 /profile
"""


@main.route("/")
def index():
    return render_template("index.html")

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!add form', form)
    # ImmutableMultiDict([('title', '的撒发射点法大师傅大师傅')])
    t = Todo.inserTodo(form)
    print(t)
    return redirect(url_for('.index'))

@main.route("/all")
def all():
    import json
    list = Todo.getAll()
    return (list)

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

#
# @main.route("/register", methods=['POST'])
# def register():
#     form = request.form
#     # 用类函数来判断
#     u = User.register(form)
#     return redirect(url_for('.index'))
#
#
# @main.route("/login", methods=['POST'])
# def login():
#     form = request.form
#     u = User.validate_login(form)
#     if u is None:
#         # 转到 topic.index 页面
#         return redirect(url_for('.index'))
#     else:
#         # session 中写入 user_id
#         ''''''
#         session['user_id'] = u.id
#         # 设置 cookie 有效期为 永久
#         session.permanent = True
#         return redirect(url_for('todo.index'))
#
#
# @main.route('/profile')
# def profile():
#     u = current_user()
#     if u is None:
#         return redirect(url_for('.index'))
#     else:
#         return render_template('profile.html', user=u)


# def allow_file(filename):
#     suffix = filename.split('.')[-1]
#     from config import accept_user_file_type
#     return suffix in accept_user_file_type
#
#
# @main.route('/addimg', methods=["POST"])
# def add_img():
#     u = current_user()
#
#     if u is None:
#         return redirect(url_for(".profile"))
#
#     if 'file' not in request.files:
#         return redirect(request.url)
#
#     file = request.files['file']
#     if file.filename == '':
#         return redirect(request.url)
#
#     if allow_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(user_file_director, filename))
#         u.user_image = filename
#         u.save()
#
#     return redirect(url_for(".profile"))
#
#
# @main.route("/uploads/<filename>")
# def uploads(filename):
#     return send_from_directory(user_file_director, filename)
