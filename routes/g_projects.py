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
from models.project import Project
from routes.index import current_user
main = Blueprint('g_projects', __name__)

@main.route('/<gid>/projects')
def index(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    return render_template("g_projects.html", user=u, group=g)

@main.route('/<gid>/projects/all')
def all(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    list = Project.getAll(None, g)
    return (list)

@main.route("/<gid>/projects/add", methods=['POST'])
def add(gid):
    form = request.form
    print('!!project add form', form)
    # ImmutableMultiDict([('title', '的撒发射点法大师傅大师傅')])
    u = current_user()
    g = Group.get_one_by(group_id=gid)

    t = Project.inserProject(form, u, g)
    return t