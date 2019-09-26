import uuid

from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

blue = Blueprint('first_blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'Hello'



# from flask_wtf import FileField, FileRequired, FileAllowed
from flask import send_from_directory

class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg','jpeg','png','gif'])])
    submit = SubmitField()


def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

@blue.route('/uploaded-images')
def show_images():
    return render_template('uploaded.html')

@blue.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)


@blue.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename =random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        flash('Upload success.')
        session['filenames'] = [filename]
        return redirect(url_for('show_images'))
    return render_template('upload.html', form = form)