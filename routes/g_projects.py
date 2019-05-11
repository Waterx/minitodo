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
main = Blueprint('g_projects', __name__)

@main.route('/<gid>/projects')
def index(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    return render_template("g_index.html", user=u, group=g)