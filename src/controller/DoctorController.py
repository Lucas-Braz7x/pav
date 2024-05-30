from src.service.DoctorService import DoctorService
from flask_restful import Resource
from flask import request, jsonify

class DoctorController(Resource):
    def __init__(self):
        self.doctorService = DoctorService()

    def get(self, doctor_id=None, name=None):
        if(name):
            return self.doctorService.findByName(name)
        
        return self.doctorService.find(doctor_id)

    def post(self):
        data = request.get_json()
        return self.doctorService.create(data)

    def put(self, doctor_id):
        data = request.get_json()
        return self.doctorService.update(doctor_id, data)

    def delete(self, doctor_id):
        self.doctorService.delete(doctor_id)
        return jsonify({"message": "Doctor deleted"})
