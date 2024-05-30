import re
from marshmallow import Schema, ValidationError, fields, validates

class DoctorResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    specialty = fields.Str()
    crm = fields.Str()

class DoctorRequestSchema(Schema):
    name = fields.Str(required=True)
    specialty = fields.Str(required=True)
    crm = fields.Int(required=True)

    @validates("name")
    def validate_name(self, value):
        if not re.match(pattern=r"^[a-zA-Z0-9_]+$", string=value):
            raise ValidationError(
                "Value must contain only alphanumeric and underscore characters."
            )