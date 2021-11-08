from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import validators, ValidationError
from wtforms.validators import Email
class ContactForm(Form):
  name = StringField("Name",  [validators.Required("Please enter your name.")])
  email = StringField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = StringField("Subject",  [validators.Required("Please enter a Subject title for us to understand.")])
  message = TextAreaField("Message",  [validators.Required("Please enter the complete message.")])
  submit = SubmitField("Send")
