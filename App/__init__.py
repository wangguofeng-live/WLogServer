from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_blue


def create_app():
    app = Flask(__name__, template_folder=settings.TEMPLATE_FOLDER, static_folder=settings.STATIC_FOLDER)

    # 初始化配置
    app.config.from_object(envs.get('develop'))

    # 注册蓝图
    init_blue(app)

    # 初始化插件
    init_ext(app)

    return app