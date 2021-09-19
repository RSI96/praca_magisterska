from flask.cli import FlaskGroup
from flask_cors import CORS, cross_origin
from flask import request, jsonify
import os, json
from dataProcessing import get_column_names, runMLAlghoritms
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
def addSelectedColumnName():
   if request.method == 'POST':
      data = request.get_json()
      columnName = data['column_name']
      datasetName = data['dataset_name']
      db.session.add(DatasetsInfo(columnName=columnName, datasetName=datasetName))
      db.session.commit()
      return jsonify(success=True)

@app.route("/getDistinctPairs", methods=['GET'])
def getDistinctPairs():

    qryresult = DatasetsInfo.query.distinct()
    return jsonify([i.serialize for i in qryresult.all()])

@app.route('/runML', methods = ['POST'])
def runML():
   if request.method == 'POST':
      data = request.get_json()
      columnName = data['column_name']
      datasetName = data['dataset_name']
      alghoritmName = data['alghoritm_name']

      result, y_test, ypred_lr = runMLAlghoritms(columnName, datasetName, alghoritmName)

      print(y_test)
      print(ypred_lr)

      return  json.dumps({
        'result': result,
        'y_test': [int(x) for x in y_test],
        'y_pred': [int(x) for x in ypred_lr]
    })

if __name__ == "__main__":
    cli()