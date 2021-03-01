from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired()], \
     render_kw={'placeholder': "Enter New Task Here"})
    submit =  SubmitField("OK")

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField(label="Sign In")