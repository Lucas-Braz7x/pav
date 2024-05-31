from src.service.AppointmentService import AppointmentService
from src.schemas.AppointmentSchema import  AppointmentResponseSchema, AppointmentRequestSchema, AppointmentListResponseSchema
from flask_apispec import use_kwargs, marshal_with
from src.utils.determineSchema import determineSchema
from flask_restful import Resource, abort
from flask import request

class AppointmentController(Resource):
    def __init__(self):
        self.appointmentService = AppointmentService()

    def get(self, appointment_id=None, date=None):
        appointment = {}

        if(date):
            appointment = self.appointmentService.findByDate(date)
        else: 
            appointment = self.appointmentService.find(appointment_id)

        response = determineSchema(name='appointments', data=appointment, schema=AppointmentResponseSchema, listSchema=AppointmentListResponseSchema)
    
        return response

    @use_kwargs(AppointmentRequestSchema, location=("json"))
    @marshal_with(AppointmentResponseSchema)
    def post(self, **data):
        return self.appointmentService.create(data)

    @use_kwargs(AppointmentRequestSchema, location=("json"))
    @marshal_with(AppointmentResponseSchema)
    def put(self, appointment_id, **data):
        return self.appointmentService.update(appointment_id, data)

    def delete(self, appointment_id):
        return self.appointmentService.delete(appointment_id)
