from flask import Blueprint
from flask import flash
from flask import render_template

bp = Blueprint("articles", __name__)

@bp.route("/articles/")
def articles():
    return render_template('articles.html')

