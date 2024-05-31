from src.service.MedicalRecordService import MedicalRecordService
from src.schemas.MedicalRecordSchema import MedicalRecordRequestSchema, MedicalRecordResponseSchema, MedicalRecordListResponseSchema
from src.utils.determineSchema import determineSchema
from flask_restful import Resource, abort
from flask_apispec import use_kwargs, marshal_with
from flask import request, jsonify

class MedicalRecordController(Resource):
    def __init__(self):
        self.medicalRecordService = MedicalRecordService()

    def get(self, medicalRecord_id=None):
        medicalRecord = self.medicalRecordService.find(medicalRecord_id)

        response = determineSchema(name='medicalRecords', data=medicalRecord, schema=MedicalRecordResponseSchema, listSchema=MedicalRecordListResponseSchema)

        return response

    @use_kwargs(MedicalRecordRequestSchema, location=("json"))
    @marshal_with(MedicalRecordResponseSchema)
    def post(self, **data):
        return self.medicalRecordService.create(data)

    @use_kwargs(MedicalRecordRequestSchema, location=("json"))
    @marshal_with(MedicalRecordResponseSchema)
    def put(self, medicalRecord_id, **data):
        return self.medicalRecordService.update(medicalRecord_id, data)

    def delete(self, medicalRecord_id):
        self.medicalRecordService.delete(medicalRecord_id)
        return jsonify({"message": "Medical Record deleted"})
