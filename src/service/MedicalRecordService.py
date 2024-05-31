from src.repository.MedicalRecordRepository import MedicalRecordRepository
from src.repository.ConsultationRepository import ConsultationRepository
from src.view.ModelView import ModelView
from flask_restful import request, abort

class MedicalRecordService:
    def __init__(self):
        self.medicalRecordRepository = MedicalRecordRepository()
        self.consultationRepository = ConsultationRepository()
        self.medicalRecordModelView = ModelView()

    def validation(self, data):
        request_method = request.method
        print(request_method)


        consultationId = data.get('consultationId')

        if (request_method == "POST" and not consultationId):
            abort(400, message="Consultation ID and Date are required")

        if(consultationId):
            self.consultationRepository.getById(consultationId)

            consultations = self.medicalRecordRepository.getAll()
            existConsultation = [consultation for consultation in consultations if consultation.consultationId == consultationId]

            if(len(existConsultation)):
                abort(400, message=f"Medical Record already exist for consultation id = {consultationId}")
        


    def find(self, medicalRecordId=None):
        medicalRecord = {}

        if medicalRecordId:
            medicalRecord = self.medicalRecordRepository.getById(medicalRecordId)
        else: 
            medicalRecord = self.medicalRecordRepository.getAll()
        
        return medicalRecord
    
    def create(self, data):
        self.validation(data)

        return self.medicalRecordRepository.create(data)
    
    def update(self, medicalRecordId, data):
        self.validation(data)

        return self.medicalRecordRepository.update(medicalRecordId, data)

    def delete(self, medicalRecordId):
        self.medicalRecordRepository.delete(medicalRecordId)
        return self.medicalRecordModelView.registerIdDeleted(message="medicalRecord deleted")

