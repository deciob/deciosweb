from flask_frozen import Freezer
import flaskr

app = flaskr.create_app()

app.config["FREEZER_DESTINATION"] = "../build"
app.config["FREEZER_STATIC_IGNORE"] = "*.css"
app.config['FREEZER_BASE_URL'] = "https://deciob.github.io/deciosweb/"

freezer = Freezer(app)

# def url_generator():
#     for article in articles:
#         yield f'/article-{article.id}.html'
#
# freezer.register_generator(url_generator)

if __name__ == '__main__':
    freezer.freeze()
