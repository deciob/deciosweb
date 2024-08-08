from flask_frozen import Freezer
import flaskr

app = flaskr.create_app()

freezer = Freezer(app)
import pdb; pdb.set_trace()

if __name__ == '__main__':
    freezer.freeze()
