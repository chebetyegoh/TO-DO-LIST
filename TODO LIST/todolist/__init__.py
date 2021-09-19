from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']='204a0cb0e8f0815b4cf5baae3c58c396'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///todolist.db'
db = SQLAlchemy(app)


from todolist import routes