from src.repository.AppointmentRepository import AppointmentRepository
from src.view.ModelView import ModelView
from src.utils.addDay import addDay
from flask_restful import abort
from datetime import datetime

class AppointmentService:
    def __init__(self):
        self.appointmentRepository = AppointmentRepository()
        self.appointmentModelView = ModelView()

    def validation(self, data):
        consultationId = data.get('consultationId')

        if not consultationId:
            abort(400, message="Consultation ID and Date are required")

    def find(self, appointmentId=None):
        if appointmentId:
            appointment = self.appointmentRepository.getById(appointmentId)
            return self.appointmentModelView.formatter(appointment)
        
        appointments = self.appointmentRepository.getAll()
        return self.appointmentModelView.formatterAll(appointments)
    
    def findByDate(self, date):
        appointments = self.appointmentRepository.getAll()
        filtered_appointments = []

        for appointment in appointments:
            appointment_date_string = str(appointment.date)
            if date in appointment_date_string:
                filtered_appointments.append(appointment)

        return self.appointmentModelView.formatterAll(filtered_appointments)
    
    def findByConsultationId(self, consultationId):
        appointment = self.appointmentRepository.findByConsultationId(consultationId)
        return self.appointmentModelView.formatter(appointment)

    def findByConsultationId(self, appointmentId):
        return self.entity.query.filter_by(appointmentId=appointmentId).all()
    
    def create(self, data):
        date = data.get("date")

        self.validation(data)

        if(not date):
            print(addDay(datetime.now()))
            #abort(400, message="Consultation ID and Date are required")

        
        newAppointment = self.appointmentRepository.create(data)

        return self.appointmentModelView.formatter(newAppointment, message="appointment created")
    
    def update(self, appointmentId, data):
        
        self.validation(data)

        updatedAppointment = self.appointmentRepository.update(appointmentId, data)
        
        return self.appointmentModelView.formatter(updatedAppointment, message="appointment updated")

    def delete(self, appointmentId):
        self.appointmentRepository.delete(appointmentId)
        return self.appointmentModelView.registerIdDeleted(message="appointment deleted")
    
    def deleteByConsultationId(self, consultationId):
        appointment = self.appointmentRepository.findByConsultationId(consultationId)

        if(len(appointment)):
            self.appointmentRepository.delete(appointment[0].id)
            #return self.appointmentModelView.registerIdDeleted(message="appointment deleted")

