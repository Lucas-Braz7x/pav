import re
from marshmallow import Schema, ValidationError, fields, validates

class PatientResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    cpf = fields.Str()
    age = fields.Int()
    historicoMedico = fields.Bool()

class PatientListResponseSchema(Schema):
    patients = fields.List(fields.Nested(PatientResponseSchema))

class PatientRequestSchema(Schema):
    name = fields.Str(required=True)
    cpf = fields.Str(required=True)
    age = fields.Int(required=True)
    historicoMedico = fields.Bool(required=False)

    @validates("cpf")
    def validate_cpf(self, value):
        # CPF validation logic here
        if not re.match(pattern=r"^\d{11}$", string=value):
            raise ValidationError(
                "CPF must contain exactly 11 digits."
            )

    @validates("age")
    def validate_age(self, value):
        if value < 0:
            raise ValidationError(
                "Age must be a positive integer."
            )