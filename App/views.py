from flask import Blueprint, render_template, request


blue = Blueprint('first_blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Hello'