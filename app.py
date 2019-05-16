from flask import Flask

import config


# web framework
# web application
# __main__
app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可以
app.secret_key = config.secret_key


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
from routes.index import main as index_routes
from routes.projects import main as projects_routes
from routes.tags import main as tags_routes
from routes.notes import main as notes_routes
from routes.groups import main as groups_routes

from routes.g_index import main as g_index_routes
from routes.g_projects import main as g_projects_routes
from routes.g_tags import main as g_tags_routes
from routes.g_notes import main as g_notes_routes
from routes.g_members import main as g_members_routes
from routes.g_performance import main as g_performance_routes

app.register_blueprint(index_routes)
app.register_blueprint(projects_routes, url_prefix='/projects')
app.register_blueprint(tags_routes, url_prefix='/tags')
app.register_blueprint(notes_routes, url_prefix='/notes')
app.register_blueprint(groups_routes, url_prefix='/groups')

app.register_blueprint(g_index_routes, url_prefix='/groups')
app.register_blueprint(g_projects_routes, url_prefix='/groups')
app.register_blueprint(g_tags_routes, url_prefix='/groups')
app.register_blueprint(g_notes_routes, url_prefix='/groups')
app.register_blueprint(g_members_routes, url_prefix='/groups')
app.register_blueprint(g_performance_routes, url_prefix='/groups')
# app.register_blueprint(reply_routes, url_prefix='/reply')
# app.register_blueprint(board_routes, url_prefix='/board')
# app.register_blueprint(mail_routes, url_prefix='/mail')


# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='localhost',
        port=3000,
    )
    app.run(**config)
