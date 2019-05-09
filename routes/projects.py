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
from routes.index import current_user
from utils import log
main = Blueprint('projects', __name__)

@main.route("/")
def index():
    u = current_user()
    if u is not None:
        # 若有用户
        return render_template("projects.html", user=u)
    else:
        # 若无用户
        return redirect(url_for('index.index'))

@main.route("/all")
def all():
    u = current_user()
    list = Project.getAll(u)
    return (list)

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!project add form', form)
    # ImmutableMultiDict([('title', '的撒发射点法大师傅大师傅')])
    u = current_user()
    t = Project.inserProject(form, u)
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
