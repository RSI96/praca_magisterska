from flask_sqlalchemy import SQLAlchemy
from src import app

db = SQLAlchemy(app)

class DatasetsInfo(db.Model):
    __tablename__ = "datasetsInfo"

    id = db.Column(db.Integer, primary_key=True)
    columnName = db.Column(db.String(128), nullable=False)
    datasetName = db.Column(db.String(128), nullable=False)

    def __init__(self, columnName, datasetName):
        self.columnName = columnName
        self.datasetName = datasetName

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'column_name': self.columnName,
           'dataset_name'  : self.datasetName
       }