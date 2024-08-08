from flask import Flask
from flask import url_for
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/articles/")
def articles():
    return render_template('articles.html')

@app.route("/visualisations/")
def visualisations():
    return render_template('visualisations.html')

with app.test_request_context():
    print(url_for('hello_world'))
    #print(url_for('hello', name="Decio"))
