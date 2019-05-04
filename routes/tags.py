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
from utils import log
main = Blueprint('tags', __name__)

@main.route("/")
def index():
    return render_template("tags.html")

@main.route("/all")
def all():
    list = Tag.getAll()
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!tag add form', form)
    t = Tag.inserTag(form)
    return t

'''本函数注意在删除tag的时候，包含tag的todo只删除tag字段'''
@main.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    print('!!tag delete json', json['tag_id'])
    result_status = Tag.delTag(json)
    print(result_status)
    return result_status