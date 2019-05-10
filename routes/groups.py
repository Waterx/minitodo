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
    list = Group.getAll(u)
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!tag add form', form)
    u = current_user()
    g = Group.addGroup(form, u)
    return g