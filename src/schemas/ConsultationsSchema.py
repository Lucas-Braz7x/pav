from marshmallow import Schema, fields, validate
from src.schemas.MedicalRecordSchema import MedicalRecordResponseSchema
from src.schemas.PatientSchema import PatientResponseSchema
from src.schemas.DoctorSchema import DoctorResponseSchema 
from src.schemas.AppointmentSchema import AppointmentResponseSchema 


class ConsultationsResponseSchema(Schema):
    id = fields.Int()
    doctorId = fields.Int()
    doctor = fields.Nested(DoctorResponseSchema)
    patientId = fields.Int()
    patient = fields.Nested(PatientResponseSchema)
    completed = fields.Bool()
    medical_records = fields.List(fields.Nested(MedicalRecordResponseSchema))
    appointments = fields.List(fields.Nested(AppointmentResponseSchema))

class ConsultationsListResponseSchema(Schema):
    consultations = fields.List(fields.Nested(ConsultationsResponseSchema))

class ConsultationsRequestSchema(Schema):
    doctorId = fields.Int(required=True, validate=validate.Range(min=1))
    patientId = fields.Int(required=True, validate=validate.Range(min=1))
    completed = fields.Bool(required=True)
    date = fields.Str(required=False)

