# CMS Project by Dmitrienko, Golovina, ..
# <)
# Не редактировать FrontEnd-ерам, мало ли поломается все)!!

from flask import Flask, render_template
from route import route

app = Flask(__name__)
app.register_blueprint(route, url_prefix="")

#Routing

# @app.route("/")
# def index():
#     return render_template("index.html")

if(__name__ == "__main__"):
    app.run(debug=True) 
