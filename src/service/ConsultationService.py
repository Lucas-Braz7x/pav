from src.repository.ConsultationRepository import ConsultationRepository
from src.service.AppointmentService import AppointmentService
from src.service.PatientService import PatientService
from src.service.DoctorService import DoctorService
from src.view.ModelView import ModelView
from flask_restful import abort
from datetime import datetime


class ConsultationService:
    def __init__(self):
        self.consultationRepository = ConsultationRepository()
        self.appointmentService = AppointmentService()
        self.patientService = PatientService()
        self.doctorService = DoctorService()
        self.consultationModelView = ModelView()

    def validation(self, data):
        patientId = data.get('patientId')
        doctorId = data.get('doctorId')

        if not patientId or not doctorId:
            abort(400, message="Patient ID and Doctor ID are required")

        self.patientService.find(patient_id=patientId)
        self.doctorService.find(doctor_id=doctorId)

    def find(self, consultation_id=None):
        if consultation_id:
            consultation = self.consultationRepository.getById(consultation_id)
            return consultation
        
        consultations = self.consultationRepository.getAll()
        
        return consultations
    
    def findByDoctorName(self, doctorName):
        consultations = self.consultationRepository.getAll()
        filtered_consultations = []

        for consultation in consultations:
            print(consultation.appointments)
            if consultation.doctor and consultation.doctor.name == doctorName:
                filtered_consultations.append(consultation)

        return self.consultationModelView.formatterAll(filtered_consultations)
    
    def findByPatientName(self, patientName):
        consultations = self.consultationRepository.getAll()
        filtered_consultations = []

        for consultation in consultations:
            print(consultation.appointments)
            if consultation.doctor and consultation.patient.name == patientName:
                filtered_consultations.append(consultation)

        return self.consultationModelView.formatterAll(filtered_consultations)
    
    
    def create(self, data):
        self.validation(data)
        dateString = data.pop('date', None)

        date = None
        if(dateString):
            date = datetime.strptime(dateString, '%Y-%m-%d %H:%M:%S')

        new_consultation = self.consultationRepository.create(data)

        self.appointmentService.create({"consultationId": new_consultation.id, "date": date})

        return self.consultationModelView.formatter(new_consultation, message="Consultation created")

    def update(self, consultation_id, data):
        self.validation(data)

        updated_consultation = self.consultationRepository.update(consultation_id, data)
        
        return self.consultationModelView.formatter(updated_consultation, message="Consultation updated")

    def delete(self, consultation_id):
        self.consultationRepository.delete(consultation_id)
        self.appointmentService.deleteByConsultationId(consultationId=consultation_id)
        return self.consultationModelView.registerIdDeleted("Consultation deleted")
    
   
