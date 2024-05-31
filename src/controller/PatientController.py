from src.service.PatientService import PatientService
from src.schemas.PatientSchema import PatientRequestSchema, PatientResponseSchema, PatientListResponseSchema
from flask_restful import Resource
from flask_apispec.views import MethodResource
from src.utils.determineSchema import determineSchema
from flask_apispec import use_kwargs, marshal_with
from flask import  jsonify

class PatientController(MethodResource, Resource): 
    def __init__(self):
        self.patientService = PatientService()

    def get(self, patient_id=None, name=None):
        patient = {}

        if name:
            patient = self.patientService.findByName(name)
        else:
            patient = self.patientService.find(patient_id)

        response = determineSchema(name='patients', data=patient, schema=PatientResponseSchema, listSchema=PatientListResponseSchema)

        return response

    @use_kwargs(PatientRequestSchema, location=("json"))
    @marshal_with(PatientResponseSchema)
    def post(self, **data):
        patient  = self.patientService.create(data)
        return patient, 201

    @use_kwargs(PatientRequestSchema, location=("json"))
    @marshal_with(PatientResponseSchema)
    def put(self, patient_id, **data):
        return self.patientService.update(patient_id, data=data)

    def delete(self, patient_id):
        return self.patientService.delete(patient_id)
