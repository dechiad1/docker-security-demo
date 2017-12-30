from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class LoginForm(Form):
	user = StringField('user', validators=[DataRequired()])
	passwd = PasswordField('passwd', validators=[DataRequired()])

class PostForm(Form):
	body = TextAreaField('body', validators=[DataRequired()], widget=TextArea())
