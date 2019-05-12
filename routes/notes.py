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
from routes.index import current_user
from utils import log
main = Blueprint('notes', __name__)

@main.route("/")
def index():
    u = current_user()
    if u is not None:
        # 若有用户
        return render_template("notes.html", user=u)
    else:
        # 若无用户
        return redirect(url_for('index.index'))

@main.route("/all")
def all():
    u=current_user()
    list = Note.getAll(u, None)
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!note add form', form)
    u = current_user()
    t = Note.inserNote(form, u, None)
    return t

@main.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    print('!!note delete json', json['note_id'])
    result_status = Note.delNote(json)
    print('!!note delete json', result_status)
    return result_status