from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextArea
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = StringField('Message', widget=TextArea())
    
