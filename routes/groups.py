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

from models.group import Group
from models.todo import Todo
from routes.index import current_user
from utils import log
main = Blueprint('groups', __name__)

@main.route("/")
def index():
    u = current_user()
    if u is not None:
        # 若有用户
        return render_template("groups.html", user=u)
    else:
        # 若无用户
        return redirect(url_for('index.index'))

@main.route("/all")
def all():
    u = current_user()
    list = Group.getAll(u, None)
    return list

'''得到所有参加的群组'''
@main.route(("/p_all"))
def p_all():
    u = current_user()
    list = Group.getpall(u)
    return list

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!group add form', form)
    u = current_user()
    g = Group.addGroup(form, u)
    return g

'''用户参加群组，暂时的方法是通过groupid参加'''
@main.route('/participate', methods=['POST'])
def participate():
    form = request.form
    print("!!group participate form", form)
    u = current_user()
    g = Group.participateGroup(form, u)
    return g

