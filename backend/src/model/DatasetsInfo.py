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