from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Visits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unique_link = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())
