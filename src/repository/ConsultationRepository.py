from src.model.Consultation import Consultation
from src.repository.BaseRepository import BaseRepository

class ConsultationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Consultation)