from flask_frozen import Freezer
import flaskr

app = flaskr.create_app()

app.config["FREEZER_DESTINATION"] = "../build"
app.config["FREEZER_STATIC_IGNORE"] = "*.css"

freezer = Freezer(app)


if __name__ == '__main__':
    freezer.freeze()
