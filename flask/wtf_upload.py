from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename, redirect
import os

from wtforms import SubmitField


class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('上传')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
app.config['SECRET_KEY'] = os.environ.get(
    'SECRET_KEY') or 'hard to guess string'
app.config['UPLOAD_FOLDER'] = os.getcwd()


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    file_url = None
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_url = url_for('uploaded_file', filename=filename)
    return render_template('upload.html', form=form, file_url=file_url)


if __name__ == '__main__':
    app.run(debug=True)
