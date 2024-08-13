from flask import Blueprint
from flask import flash
from flask import render_template

bp = Blueprint("homepage", __name__)

@bp.route("/")
def homepage():
    return render_template('home.j2', )

