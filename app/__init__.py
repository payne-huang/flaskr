# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir
app = Flask(__name__)
app.config.from_object('config') #载入配置
db = SQLAlchemy(app)
# from app import views,models
import  views,models

