from db.connect import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    historicoMedico = db.Column(db.Boolean, nullable=True)