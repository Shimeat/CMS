# CMS Project by Dmitrienko, Golovina, ..
# <)
# Не редактировать FrontEnd-ерам, мало ли поломается все)!!

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import *
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(os.path.dirname(os.path.abspath(__name__)), 'la.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# Modules
@app.route('/')
def index():
    return render_template('index.html', groups_platform=GroupsPlatforms.query.all(), platforms=Platforms.query.all())


if(__name__ == "__main__"):
    app.run(debug=True) 
