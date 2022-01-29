from flask import Blueprint, render_template

route = Blueprint("route", __name__, template_folder="templates", static_folder="assets", static_url_path="assets")


# Base Routing

@route.route('/')
def index():
    return render_template('index.html')