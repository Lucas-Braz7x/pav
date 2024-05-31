from db.connect import db
from sqlalchemy.orm import relationship


class Consultation(db.Model):
    __tablename__ = 'consultation'

    id = db.Column(db.Integer, primary_key=True)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    patientId = db.Column(db.Integer, db.ForeignKey('patient.id', ondelete="CASCADE"), nullable=False)
    doctorId = db.Column(db.Integer, db.ForeignKey('doctor.id', ondelete="CASCADE"), nullable=False)

    patient = relationship('Patient', back_populates='consultations')
    doctor = relationship('Doctor', back_populates='consultations')
    
    medical_records = relationship("MedicalRecord", back_populates="consultation", cascade="all, delete-orphan", passive_deletes=False)

