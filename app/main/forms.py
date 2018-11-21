from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from ..models import User
from wtforms import ValidationError
from wtforms.validators import Required, Email, EqualTo

class CommentsForm(FlaskForm):
    comments = TextAreaField('Pitch Comments', validators=[Required()])
    submit = SubmitField('Submit')

class ContentForm(FlaskForm):
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('SUBMIT')


class PitchForm(FlaskForm): #create a class that inherits from FlaskForm class
    Category = SelectField('Category', choices =[('product','product'),('pickuplines','pickuplines'),('interview','interview'),('promotion','promotion')],validators=[Required()])
    Pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')