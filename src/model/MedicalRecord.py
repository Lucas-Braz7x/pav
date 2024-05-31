from db.connect import db

class MedicalRecord(db.Model):
    __tablename__ = 'medical_record'
    id = db.Column(db.Integer, primary_key=True)
    consultationId = db.Column(db.Integer, db.ForeignKey('consultation.id', ondelete="CASCADE"), nullable=False)
    diagnosis = db.Column(db.Text, nullable=True)
    prescription = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    consultation = db.relationship('Consultation', back_populates='medical_records')

