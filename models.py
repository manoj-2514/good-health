from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    bmi = db.Column(db.Float)
    bmi_status = db.Column(db.String(50))
    lifestyle = db.Column(db.String(50))
    stress = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
