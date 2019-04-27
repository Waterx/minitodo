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