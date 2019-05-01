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
from models.todo import Todo
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

'''本函数注意在删除项目的时候，项目内todo也全部删除'''
@main.route("/delete", methods=['POST'])
def delete():
    json = request.get_json()
    print('!!project delete json', json['project_id'])
    Todo.delTodobyProject(json['project_id'])
    result_status = Project.delProject(json)
    print(result_status)
    return result_status

@main.route("/gettodoinproject", methods=['POST'])
def getTodoInProject():
    json = request.get_json()
    print('!!project gettodoinproject json', json['project_id'])
    list = Todo.getTodobyProject(json['project_id'])
    print('!!project gettodoinproject list', list)
    return list
