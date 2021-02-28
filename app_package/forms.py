from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TaskForm(FlaskForm):
    name = StringField('Task Name', render_kw={'placeholder': "Enter Task Here"})
    submit =  SubmitField("OK")