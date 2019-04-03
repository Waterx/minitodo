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

@main.route("/add", methods=['POST'])
def add():
    form = request.form
    print('!!project add form', form)
    # ImmutableMultiDict([('title', '的撒发射点法大师傅大师傅')])
    t = Project.inserProject(form)
    return t