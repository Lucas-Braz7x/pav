from db.connect import db
from src.utils.addDay import addDay
from datetime import datetime

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    consultationId = db.Column(db.Integer, db.ForeignKey('consultation.id', ondelete="CASCADE"), nullable=True)

    Consultation = db.relationship('Consultation', backref=db.backref('appointments', lazy=True))

