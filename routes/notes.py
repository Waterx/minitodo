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

from utils import log
main = Blueprint('notes', __name__)

@main.route("/")
def index():
    return render_template("notes.html")

@main.route("/all")
def all():
    list = Note.getAll()
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!note add form', form)
    t = Note.inserNote(form)
    return t

@main.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    print('!!note delete json', json['note_id'])
    result_status = Note.delNote(json)
    print('!!note delete json', result_status)
    return result_status