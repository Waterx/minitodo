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

from models.project import Project
from utils import log
main = Blueprint('projects', __name__)

@main.route("/")
def index():
    return render_template("projects.html")

@main.route("/all")
def all():
    list = Project.getAll()
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!project add form', form)
    # ImmutableMultiDict([('title', '的撒发射点法大师傅大师傅')])
    t = Project.inserProject(form)
    return t

@main.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    print('!!!!!!!!!',json)
    print('!!project delete json', json['project_id'])
    result_status = Project.delProject(json)
    print(result_status)
    return result_status