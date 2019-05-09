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

from models.tag import Tag
from models.todo import Todo
from routes.index import current_user
from utils import log
main = Blueprint('tags', __name__)

@main.route("/")
def index():
    u = current_user()
    if u is not None:
        # 若有用户
        return render_template("tags.html", user=u)
    else:
        # 若无用户
        return redirect(url_for('index.index'))
@main.route("/all")
def all():
    u = current_user()
    list = Tag.getAll(u)
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!tag add form', form)
    u = current_user()
    t = Tag.inserTag(form, u)
    return t

'''本函数注意在删除tag的时候，包含tag的todo只删除tag字段'''
@main.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    print('!!tag delete json', json['tag_id'])
    result_status = Tag.delTag(json)
    print(result_status)
    return result_status

@main.route("/gettodointag", methods=['POST'])
def getTodoInTag():
    json = request.get_json()
    print('!!tag gettodointag json', json['tag_id'])
    list = Todo.getTodobyTag(json['tag_id'])
    print('!!tag gettodointag list', list)
    return list