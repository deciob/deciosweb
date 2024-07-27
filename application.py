from flask import Flask
from flask import url_for
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route("/<name>")
def hello(name):
    #return f"Hello, {escape(name)}!"
    return render_template('hello.html', person=name)

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('hello', name="Decio"))
