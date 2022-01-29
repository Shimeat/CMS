# CMS Project by Dmitrienko, Golovina, ..
# <)
# Не редактировать FrontEnd-ерам, мало ли поломается все)!!

from flask import Flask

app = Flask(__name__)

#Routing

@app.route("/")
def index():
    return "<h1>Ебать у вас тут CMS</h1>"

if(__name__ == "__main__"):
    app.run(debug=True)

