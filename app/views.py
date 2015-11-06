# -*- coding: utf-8 -*-

from  app import app,db
from flask import render_template,flash,redirect,session,url_for,request,g
from models import User,Post,ROLE_USER,ROLE_ADMIN

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adduser/<nickname>/<email>')
def adduser(nickname,email):
    u = User(nickname,email)
    try:
        db.session.add(u)
        db.session.commit()
    except Exception,e:
        return 'something go wrong'

@app.route('/getuser/<nickname>')
def getuser(nickname):
    user = User.