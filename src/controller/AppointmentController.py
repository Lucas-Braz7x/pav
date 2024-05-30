from src.service.AppointmentService import AppointmentService
from flask_restful import Resource, abort
from flask import request

class AppointmentController(Resource):
    def __init__(self):
        self.appointmentService = AppointmentService()

    def get(self, appointment_id=None, date=None):
        if(date):
            return self.appointmentService.findByDate(date)
        return self.appointmentService.find(appointment_id)

    def post(self):
        data = request.get_json()
        return self.appointmentService.create(data)

    def put(self, appointment_id):
        data = request.get_json()
        return self.appointmentService.update(appointment_id, data)

    def delete(self, appointment_id):
        return self.appointmentService.delete(appointment_id)
