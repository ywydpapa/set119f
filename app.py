from flask import Flask, request, render_template, make_response
import json
from time import time, localtime
import pymysql

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def start_here():  # put application's code here
    f = open('static/setcont.ini','r')
    return render_template("index.html", result=f.readline())

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
