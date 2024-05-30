from src.model.Patient import Patient
from src.repository.BaseRepository import BaseRepository

class PatientRepository(BaseRepository):
    def __init__(self):
        super().__init__(Patient)

    def getByName(self, name):
        return self.entity.query.filter_by(name=name).all()
