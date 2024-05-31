from src.repository.AppointmentRepository import AppointmentRepository
from src.view.ModelView import ModelView
from flask_restful import abort
from datetime import datetime

class AppointmentService:
    def __init__(self):
        self.appointmentRepository = AppointmentRepository()
        self.appointmentModelView = ModelView()

    def validation(self, data):
        consultationId = data.get('consultationId')
        date = data.get("date")

        if isinstance(date, str):
            data["date"] = datetime.strptime(date, '%Y-%m-%d %H:%M')
        elif isinstance(date, datetime):
            data["date"] = date
        else:
            abort(400, message="Date field must be a string or a datetime object")

        if not consultationId:
            abort(400, message="Consultation ID and Date are required")

    def find(self, appointmentId=None):
        if appointmentId:
            appointment = self.appointmentRepository.getById(appointmentId)
            return appointment
        
        appointments = self.appointmentRepository.getAll()
        return appointments
    
    def findByDate(self, date):
        appointments = self.appointmentRepository.getAll()
        filtered_appointments = []

        for appointment in appointments:
            appointment_date_string = str(appointment.date)
            if date in appointment_date_string:
                filtered_appointments.append(appointment)

        return filtered_appointments
    
    def findByConsultationId(self, consultationId):
        appointment = self.appointmentRepository.findByConsultationId(consultationId)
        return appointment

    def findByConsultationId(self, appointmentId):
        return self.entity.query.filter_by(appointmentId=appointmentId).all()
    
    def create(self, data):
        date = data.get("date")

        self.validation(data)
        
        return self.appointmentRepository.create(data)
    
    def update(self, appointmentId, data):
        
        self.validation(data)

        return self.appointmentRepository.update(appointmentId, data)

    def delete(self, appointmentId):
        self.appointmentRepository.delete(appointmentId)
        return self.appointmentModelView.registerIdDeleted(message="appointment deleted")
    
    def deleteByConsultationId(self, consultationId):
        appointment = self.appointmentRepository.findByConsultationId(consultationId)

        if(len(appointment)):
            self.appointmentRepository.delete(appointment[0].id)
            #return self.appointmentModelView.registerIdDeleted(message="appointment deleted")

