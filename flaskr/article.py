from flask import Blueprint
from flask import flash
from flask import render_template

bp = Blueprint("article", __name__)

@bp.route("/articles/<int:article>.html")
def article(article):
    return render_template(f'articles/article-{article}.html')

