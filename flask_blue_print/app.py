# -*- coding: utf-8 -*-
from flask import Flask
from admin import admin_blue

app = Flask(__name__)

app.register_blueprint(admin_blue)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
