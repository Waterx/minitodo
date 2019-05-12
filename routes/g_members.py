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
import json
from models.group import Group
from models.todo import Todo
from models.tag import Tag
from routes.index import current_user
main = Blueprint('g_members', __name__)

@main.route('/<gid>/members')
def index(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    return render_template("g_members.html", user=u, group=g)

@main.route('/<gid>/members/all')
def all(gid):
    u = current_user()
    gu = Group.get_one_by(group_id=gid).users
    list = []
    for g in gu:
        t = dict(
            name=g.name,
            icon=g.icon,
            email=g.email
        )
        list.append(t)
    print(list)
    return json.dumps(list)