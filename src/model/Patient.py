from sqlalchemy.orm import relationship
from db.connect import db

class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    historicoMedico = db.Column(db.Boolean, nullable=True)

    consultations = relationship("Consultation", back_populates="patient", cascade="all, delete", passive_deletes=True)
