from src.model.Appointment import Appointment
from src.repository.BaseRepository import BaseRepository

class AppointmentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Appointment)

    def findByConsultationId(self, consultationId):
        return self.entity.query.filter_by(consultationId=consultationId).all()
