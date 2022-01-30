# CMS Project by Dmitrienko, Golovina, ..
# <)
# Не редактировать FrontEnd-ерам, мало ли поломается все)!!

from flask import Flask, render_template
from route import route
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(os.path.dirname(os.path.abspath(__name__)), 'la.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# Modules
app.register_blueprint(route, url_prefix="")


if(__name__ == "__main__"):
    app.run(debug=True) 
