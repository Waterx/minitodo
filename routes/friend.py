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
from models.user import User
from utils import log
import json
main = Blueprint('friend', __name__)

@main.route("/")
def index():
    u = current_user()
    if u is not None:
        # 若有用户
        return render_template("friend.html", user=u)
    else:
        # 若无用户
        return redirect(url_for('index.index'))

@main.route("/all")
def all():
    u=current_user()
    list = User.get_all_friend(u)
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!friend add form', form)
    u = current_user()
    t = User.addfriend(form, u)
    return redirect(url_for('.index'))

@main.route("/chat", methods=['POST'])
def chat():
    u = current_user()
    form = request.form
    print('!!friend chat form', form)
    t = Chat.add(form, u.user_id, form['userto'])
    return t

@main.route("/chatall", methods=['POST'])
def chatall():
    u = current_user()
    form = request.get_json()
    print('!!friend chatall form', form)
    t = Chat.chatall(u.user_id, form['userto'])
    return t