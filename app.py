# CMS Project by Dmitrienko, Golovina, ..
# <)
# Не редактировать FrontEnd-ерам, мало ли поломается все)!!

from ast import Num
from aiohttp import request
from flask import Flask, redirect, render_template, abort, request, flash, url_for, session, jsonify
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from models import *
import os
import hashlib
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///la.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'lateam_DG'

ma = Marshmallow(app)

# Global Var
class UserSchema(ma.Schema):
    class Meta:
            # Fields to expose
            fields = ("id", "login", "password", "platforms")

class PlatofrmsSchema(ma.Schema):
    class Meta:
            # Fields to expose
            fields = ("id", "name", "id_head", "id_group")

class GroupsPlatformsSchema(ma.Schema):
    class Meta:
            # Fields to expose
            fields = ("id", "name")      

class AdminsSchema(ma.Schema):
    class Meta:
            # Fields to expose
            fields = ("id", "login", "password", "status", "permissions", "icons") 

user_schema = UserSchema()
platform_schema = PlatofrmsSchema()
gorups_platform_schema = GroupsPlatformsSchema()
admins_schema = AdminsSchema()


db = SQLAlchemy(app)

def login_required(type):
    if type == 'admin':
        if (session.get('admin_auth')):
            return True
        else:
            return redirect(url_for('admin_index'))
    else:
        if (session.get('user_auth')):
            return True
        else:
            return redirect(url_for('index'))

def logout_required(type):
    if type == 'admin':
        if (session.get('admin_auth') == None):
            return True
        else:
            return 'you are login'
    else:
        if (session.get('user_auth') == None):
            return True
        else:
            return 'you are login'

# Modules
@app.route('/')
def index():
        return render_template('index.html', groups_platform=GroupsPlatforms.query.all(), platforms=Platforms.query.all())

@app.route('/s/<int:sel>')
def index_select(sel=None):
    if (Num(sel) and Platforms.query.get(sel)):
        return render_template('index.html', groups_platform=GroupsPlatforms.query.all(), platforms=Platforms.query.all(), sel=sel)
    abort(404)

# Admin Routing

@app.route('/admin', methods=["POST", "GET"])
def admin_index():
    if request.method == 'GET':
        return render_template('admin/login.html')
    else:
        login_admin = request.form['login']
        password_admin = request.form['password']
        if (login_admin and password_admin):
            query = Admins.query.filter_by(login=login_admin, password=password_admin).first()
            if (query != None):
                session['admin_auth'] = True
                session['admin'] = admins_schema.dump(query)
                current_admin = session.get('admin')
                #return '<h1>'+str(current_admin)+'</h1>'
                return current_admin['login']
            else:
                flash('Неверный логин или пароль')
                return redirect(url_for('admin_index'))

@app.route('/admin/logout')
def admin_logout():
    login_required('admin')
    session.pop('admin_auth')
    session.pop('admin')
    return redirect(url_for('admin_index'))


if(__name__ == "__main__"):
    app.run(debug=True) 
