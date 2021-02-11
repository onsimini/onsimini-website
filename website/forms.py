from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = TextField('Title', [DataRequired()])
    content = TextField('Content',[DataRequired()])
    submit = SubmitField('Submit')

class SubmitForm(FlaskForm):
    submit = SubmitField('Submit')
