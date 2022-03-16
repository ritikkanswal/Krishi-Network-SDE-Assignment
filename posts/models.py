from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from datetime import datetime
from . import db
import pytz

IST = pytz.timezone('Asia/Kolkata')


class twitter_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80))
    coordinates = db.Column(Geometry('POINT'))
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, text,coordinates):
        self.text = text
        self.coordinates=coordinates

