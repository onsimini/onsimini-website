from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = TextField('Title', [DataRequired()])
    body = TextField('Content',[DataRequired()])
    submit = SubmitField('Submit')
