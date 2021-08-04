from flask.cli import FlaskGroup
from flask_cors import CORS, cross_origin
from flask import request
import os, json
from dataProcessing import get_column_names, rainTomorow
from src.model.DatasetsInfo import DatasetsInfo

from src import app, db

cli = FlaskGroup(app)

CORS(app)


@app.route("/", methods=['GET'])
def home():
    return {
        'hello': 'world'
    }

@app.route("/testjson", methods=['GET'])
def testjson():
    return {
        'test': 'json'
    }

@app.route('/addFile', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename(f.filename))
      f.save(os.path.join('/usr/src/app/uploadeddata/', f.filename))
      names = get_column_names(f.filename)
      names2 = [{'text': x} for x in names]
      return json.dumps(names2)

@app.route('/addSelectedColumnName', methods = ['POST'])
def parameterProtoype():
   if request.method == 'POST':
      data = request.get_json()
      columnName = data['column_name']
      datasetName = data['dataset_name']
      db.session.add(DatasetsInfo(columnName=columnName, datasetName=datasetName))
      db.session.commit()
      result = rainTomorow(columnName)
      return  {
        'result': result
    }

if __name__ == "__main__":
    cli()