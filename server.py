from flask import Flask, render_template, request, redirect, url_for
from waitress import serve
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from proccessing import process
from wtforms.validators import InputRequired
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'Abcdefg'
app.config['UPLOAD_FOLDER'] = 'filecatcher'
class UploadFile(FlaskForm):
    file = FileField("File", validators=[InputRequired(), FileAllowed(['json'])])
    submit = SubmitField("Upload File")
@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    form = UploadFile()
    return render_template('index.html',form = form)

@app.route('/test', methods = ['GET','POST'])
def get_weather():
    form = UploadFile()
    if form.validate_on_submit():
        file = form.file.data
        print(file)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        filepath = process(file.filename)
    return render_template("test.html",results=[filepath], form = form)
    # City is not found by AP

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
    app.run(debug=True)
