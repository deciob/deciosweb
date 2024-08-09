import os
from flask_frozen import Freezer
import flaskr

app = flaskr.create_app()

app.config["FREEZER_DESTINATION"] = "../build"

freezer = Freezer(app)


if __name__ == '__main__':
    freezer.freeze()
