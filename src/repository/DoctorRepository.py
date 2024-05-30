from src.model.Doctor import Doctor
from src.repository.BaseRepository import BaseRepository

class DoctorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Doctor)

    def getByName(self, name):
        return self.entity.query.filter_by(name=name).all()
