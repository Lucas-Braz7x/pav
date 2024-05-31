from sqlalchemy.orm import relationship
from db.connect import db

class Doctor(db.Model):
    __tableName__ = "doctor"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    specialty = db.Column(db.String(80), nullable=False)
    crm = db.Column(db.String(80), nullable=False)

    consultations = relationship("Consultation", back_populates="doctor", cascade="all, delete", passive_deletes=True)
