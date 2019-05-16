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

from models.chat import Chat
from models.todo import Todo
from routes.index import current_user
from utils import log
main = Blueprint('notes', __name__)

@main.route("/")
def index():
    u = current_user()
    if u is not None:
        # 若有用户
        return render_template("chat.html", user=u)
    else:
        # 若无用户
        return redirect(url_for('index.index'))

@main.route("/all")
def all():
    u=current_user()
    list = Chat.getAllc(u)
    return (list)

@main.route("/add", methods=['POST'])
def add():
    json = request.get_json()
    print('!!chat add form', json['userfrom'], json['userto'], json['title'])
    t = Chat.add(json, json['userfrom'], json['userto'])
    return t

@main.route("/readed", methods=["POST"])
def readed():
    json = request.get_json()
    t = Chat.changereaded(json['chat_id'])
    return t