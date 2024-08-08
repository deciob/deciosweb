from flask import Blueprint
from flask import flash
from flask import render_template

bp = Blueprint("visualisations", __name__)

@bp.route("/visualisations/")
def homepage():
    return render_template('visualisations.html')

