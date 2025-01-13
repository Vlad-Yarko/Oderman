from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo
# from flask_wtf.file import FileField, FileAllowed


class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=22)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm password', validators=[EqualTo('password')])
    submit = SubmitField('Submit data')


class LogIn(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=22)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit data')


# class UpdateImage(FlaskForm):
#     image = FileField('Update image', validators=[FileAllowed(['jpeg', 'jpg', 'png'])])