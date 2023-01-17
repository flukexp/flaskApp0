
from flask import Flask
app = Flask(__name__, static_folder='static')
app.config['JSON_AS_ASCII'] = False
app.config['DEBUG'] = True
app.config['SECRET_KEY']='10284942168ee2849a5c12888fd3f5ee1244f8f7590b763c'
from app import views # noqa
