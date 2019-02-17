from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Coffee and Astral Chain'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 465)
app.config['MAIL_USERNAME'] = '2e281693ef1412'
app.config['MAIL_PASSWORD'] = 'c28bee478c4f63'
mail = Mail(app)

from app import views