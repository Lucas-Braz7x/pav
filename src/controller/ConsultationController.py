from src.service.ConsultationService import ConsultationService
from src.view.ModelView import ModelView
from flask_restful import Resource, abort
from flask import request, jsonify

class ConsultationController(Resource):
    def __init__(self):
        self.consultationService = ConsultationService()
        self.consultationModelView = ModelView()

    def get(self, consultation_id=None, doctorName=None, patientName=None):
        if(doctorName):
            return self.consultationService.findByDoctorName(doctorName=doctorName)
        
        if(patientName):
            return self.consultationService.findByPatientName(patientName=patientName)
        
        consultation = self.consultationService.find(consultation_id)      

        if(isinstance(consultation, list)):
            return self.consultationModelView.formatterAll(consultation)

        return self.consultationModelView.customFormatter(modelInstance=consultation, relationModelInstances=consultation.medical_records)

    def post(self):
        data = request.get_json()
        return self.consultationService.create(data)

    def put(self, consultation_id):
        data = request.get_json()
        return self.consultationService.update(consultation_id, data)

    def delete(self, consultation_id):
        self.consultationService.delete(consultation_id)
        return jsonify({"message": "Consultation deleted"})
