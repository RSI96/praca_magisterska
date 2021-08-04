from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object("src.config.Config")

db = SQLAlchemy(app)

db.drop_all()
db.create_all()
db.session.commit()
