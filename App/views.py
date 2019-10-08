import uuid

from flask import Blueprint, render_template, request, flash, session, redirect, url_for, abort
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

from App.settings import get_upload_folder, get_filename_suffix, get_filename_list, get_file_path

blue = Blueprint('first_blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Hello Man'



# from flask_wtf import FileField, FileRequired, FileAllowed
from flask import send_from_directory

class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'txt', 'log'])])
    submit = SubmitField()


def random_filename(filename):
    new_filename = uuid.uuid4().hex + get_filename_suffix(filename)
    return new_filename

@blue.route('/file_manager')
def file_manager():
    return render_template('file_manager.html', file_names = get_filename_list())

@blue.route('/file/<filename>/', methods=['GET', 'POST'])
def get_image(filename):
    return send_from_directory(get_upload_folder(), filename)

# @blue.route('/uploads/<path:filename>')
# def get_file(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'], filename)


@blue.route('/upload', methods=['GET', 'POST'])
def upload():

    form = UploadForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('Save File ...')
            f = form.file.data
            filename = random_filename(f.filename)
            f.save(get_file_path(filename))
            flash('Upload success.')
            session['filenames'] = [filename]
        else:
            flash('Upload fail.')

    return render_template('upload.html', form=form)


