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
from models.tag import Tag
from routes.index import current_user
main = Blueprint('g_tags', __name__)

@main.route('/<gid>/tags')
def index(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    return render_template("g_tags.html", user=u, group=g)

@main.route('/<gid>/tags/all')
def all(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    list = Tag.getAll(None, g)
    return (list)

@main.route("/<gid>/tags/add", methods=['POST'])
def add(gid):
    form = request.form
    print('!!tag add form', form)
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    t = Tag.inserTag(form, u, g)
    return t