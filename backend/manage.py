from flask.cli import FlaskGroup
from flask_cors import CORS, cross_origin
from flask import request
import os


from src import app, db, User

cli = FlaskGroup(app)

CORS(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="michael@mherman.org"))
    db.session.commit()


@app.route("/", methods=['GET'])
def home():
    return {
        'hello': 'world'
    }

@app.route("/testjson", methods=['GET'])
@cross_origin()
def testjson():
    return {
        'test': 'json'
    }

@app.route('/addFile', methods = ['POST'])
@cross_origin()
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
      return 'File uploaded successfully'



if __name__ == "__main__":
    cli()