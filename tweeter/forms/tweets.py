from wtforms import TextAreaField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, StopValidation
from flask_wtf import FlaskForm


class CreateTweetForm(FlaskForm):
    text = TextAreaField('Text', [InputRequired(), Length(min=3, max=255)])