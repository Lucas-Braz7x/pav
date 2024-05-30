from db.connect import db

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consultationId = db.Column(db.Integer, db.ForeignKey('consultation.id'), nullable=False)
    diagnosis = db.Column(db.Text, nullable=True)
    prescription = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    consultation = db.relationship('Consultation', backref=db.backref('medical_records', lazy=True))
