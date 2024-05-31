from marshmallow import Schema, ValidationError, fields, validate, validates
from datetime import datetime

class AppointmentResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Str(required=True)
    consultationId = fields.Int(required=True, validate=validate.Range(min=1))

class AppointmentListResponseSchema(Schema):
    appointments = fields.List(fields.Nested(AppointmentResponseSchema)) 

class AppointmentRequestSchema(Schema):
    consultationId = fields.Int(required=True)
    date = fields.Str(required=False)

   