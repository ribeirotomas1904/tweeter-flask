from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, StopValidation
from tweeter.models.user import User


ph = PasswordHasher()

class RegisterForm(FlaskForm):
    first_name = StringField('First Name', [
        InputRequired(),
        Length(min=3, max=20),
    ])
    last_name = StringField('Last Name', [
        InputRequired(),
        Length(min=3, max=20),
    ])
    username = StringField('Username', [
        InputRequired(),
        Length(min=3, max=20),
    ])
    email = EmailField('Email', [
        InputRequired(),
    ])
    password = PasswordField('Password', [
        InputRequired(),
        Length(min=6),
    ])
    confirm_password = PasswordField('Confirm Password', [
        InputRequired(),
        EqualTo('password', message='Passwords must match.'),
    ])

    def validate_username(form, field):
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            raise ValidationError('Username has already been taken.')

    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError('Email has already been taken.')


class LoginForm(FlaskForm):
    email = EmailField('Email', [
        InputRequired()
    ])
    password = PasswordField('Password', [
        InputRequired()
    ])

    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()

        if user is None:
            raise StopValidation('Email not found.')

    def validate_password(form, field):
        user = User.query.filter_by(email=form.email.data).first()

        try:
            if user is not None:
                ph.verify(user.password, field.data)
        except VerifyMismatchError:
            raise StopValidation('Wrong password.')