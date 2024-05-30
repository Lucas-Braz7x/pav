from src.service.MedicalRecordService import MedicalRecordService
from flask_restful import Resource, abort
from flask import request, jsonify

class MedicalRecordController(Resource):
    def __init__(self):
        self.medicalRecordService = MedicalRecordService()

    def get(self, medicalRecord_id=None):
        return self.medicalRecordService.find(medicalRecord_id)

    def post(self):
        data = request.get_json()
        return self.medicalRecordService.create(data)

    def put(self, medicalRecord_id):
        data = request.get_json()
        return self.medicalRecordService.update(medicalRecord_id, data)

    def delete(self, medicalRecord_id):
        self.medicalRecordService.delete(medicalRecord_id)
        return jsonify({"message": "Consultation deleted"})
