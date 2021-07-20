from flask_sqlalchemy import SQLAlchemy
from src import app

db = SQLAlchemy(app)

class ColumnName(db.Model):
    __tablename__ = "column_names"

    id = db.Column(db.Integer, primary_key=True)
    columnName = db.Column(db.String(128), nullable=False)

    def __init__(self, columnName):
        self.columnName = columnName
