from flask import Blueprint, render_template

route = Blueprint("route", __name__, template_folder="templates")


# Base Routing

@route.route('/')
def index():
    return render_template('index.html')