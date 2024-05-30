from src.service.DoctorService import DoctorService
from src.schemas.DoctorSchema import DoctorRequestSchema, DoctorResponseSchema
from flask_restful import Resource
from flask import  jsonify
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource


class DoctorController(MethodResource, Resource):
    def __init__(self):
        self.doctorService = DoctorService()

    @marshal_with(DoctorResponseSchema)
    def get(self, doctor_id=None, name=None):
        if(name):
            return self.doctorService.findByName(name)
        
        return self.doctorService.find(doctor_id)

    @use_kwargs(DoctorRequestSchema, location=("json"))
    def post(self, **data):
        return self.doctorService.create(data)

    @use_kwargs(DoctorRequestSchema, location=("json"))
    def put(self, doctor_id, **data):
        return self.doctorService.update(doctor_id, data)

    def delete(self, doctor_id):
        self.doctorService.delete(doctor_id)
        return jsonify({"message": "Doctor deleted"})
