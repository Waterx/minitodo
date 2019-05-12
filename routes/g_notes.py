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

from models.note import Note
from models.todo import Todo
from models.group import Group
from routes.index import current_user

from utils import log
main = Blueprint('g_notes', __name__)

@main.route('/<gid>/notes')
def index(gid):
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    print(g)
    return render_template("g_notes.html", user=u, group=g)

@main.route("/<gid>/notes/all")
def all(gid):
    u=current_user()
    g = Group.get_one_by(group_id=gid)
    list = Note.getAll(None, g)
    return (list)

@main.route("/<gid>/notes/add", methods=['POST'])
def add(gid):
    form = request.form
    print('!!note add form', form)
    u = current_user()
    g = Group.get_one_by(group_id=gid)
    t = Note.inserNote(form, u, g)
    return t