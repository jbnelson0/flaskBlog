from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        #if user is anything other than none - throw error
        if user:
            raise ValidationError('That username is taken. Please choose a new username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        #if user is anything other than none - throw error
        if user:
            raise ValidationError('That email is taken. Please choose a new email.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            #if username is anything different from data in db then validate
            user = User.query.filter_by(username=username.data).first()
            #if user is anything other than none - throw error
            if user:
                raise ValidationError('That username is taken. Please choose a new username.')

    def validate_email(self, email):
        if email.data != current_user.email:
            #if email is anything different from data in db then validate
            user = User.query.filter_by(email=email.data).first()
            #if user is anything other than none - throw error
            if user:
                raise ValidationError('That email is taken. Please choose a new email.')
