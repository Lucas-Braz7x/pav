from src.model.MedicalRecord import MedicalRecord
from src.repository.BaseRepository import BaseRepository

class MedicalRecordRepository(BaseRepository):
    def __init__(self):
        super().__init__(MedicalRecord)
