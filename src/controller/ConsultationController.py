from src.service.ConsultationService import ConsultationService
from src.schemas.ConsultationsSchema import ConsultationsRequestSchema, ConsultationsResponseSchema, ConsultationsListResponseSchema
from src.utils.determineSchema import determineSchema
from flask_restful import Resource
from flask import  jsonify
from flask_apispec import use_kwargs, marshal_with
from flask_apispec.views import MethodResource

class ConsultationController(MethodResource, Resource):
    def __init__(self):
        self.consultationService = ConsultationService()

    def get(self, consultation_id=None, doctorName=None, patientName=None):
        consultation = {}
        if(doctorName):
            consultation = self.consultationService.findByDoctorName(doctorName=doctorName)
        elif(patientName):
            consultation = self.consultationService.findByPatientName(patientName=patientName)
        else: 
            consultation = self.consultationService.find(consultation_id)

        response = determineSchema(name='consultations', data=consultation, schema=ConsultationsResponseSchema, listSchema=ConsultationsListResponseSchema)

        return response

    @use_kwargs(ConsultationsRequestSchema, location=("json"))
    @marshal_with(ConsultationsResponseSchema)
    def post(self, **data):
        return self.consultationService.create(data)

    @use_kwargs(ConsultationsRequestSchema, location=("json"))
    @marshal_with(ConsultationsResponseSchema)
    def put(self, consultation_id, **data):
        return self.consultationService.update(consultation_id, data)

    def delete(self, consultation_id):
        print("TESTE")
        print(consultation_id)
        
        self.consultationService.delete(consultation_id)

        return jsonify({"message": "Consultation deleted"})
