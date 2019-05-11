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
main = Blueprint('g_index', __name__)

@main.route('/<gid>')
def index(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    return render_template("g_index.html", user=u, group=g)

@main.route("/<gid>/all")
def all(gid):
    g = Group.get_one_by(group_id=gid)
    t_list = Todo.getAll(None, g)
    return (t_list)


@main.route("/<gid>/add", methods=['POST'])
def add(gid):
    form = request.form
    print('!!add form', form)
    # ImmutableMultiDict([('title', '的撒发射点法大师傅大师傅')])
    u = current_user()
    # u代表user
    g = Group.get_one_by(group_id=gid)
    t = Todo.inserTodo(form, u, g)
    s = '.' + gid
    return redirect(url_for(".index", gid=gid))

@main.route("/<gid>/reorder", methods=['POST'])
def reorder(gid):
    form = request.form
    print('!!reorder form', form)
    result_id = Todo.reorderTodo(form)
    return redirect(url_for('.index', gid=gid))
