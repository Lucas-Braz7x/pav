from src.service.PatientService import PatientService
from flask_restful import Resource
from flask import request

class PatientController(Resource): 
    def __init__(self):
        self.patientService = PatientService()

    def get(self, patient_id=None, name=None):
        if name:
            return self.patientService.findByName(name)
            
        return self.patientService.find(patient_id)

    def post(self):
        print("Post")
        data = request.get_json()
        print(data)
        return self.patientService.create(data)

    def put(self, patient_id):
        data = request.get_json()
        return self.patientService.update(patient_id, data=data)

    def delete(self, patient_id):
        return self.patientService.delete(patient_id)
