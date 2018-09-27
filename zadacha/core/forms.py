from flask_wtf import FlaskForm
from wtforms import StringField

class TaskForm(FlaskForm):
    title = StringField('title')