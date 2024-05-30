from db.connect import db

class Consultation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    patientId = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctorId = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    

    patient = db.relationship('Patient', backref=db.backref('consultations', lazy=True))
    doctor = db.relationship('Doctor', backref=db.backref('consultations', lazy=True))
    

