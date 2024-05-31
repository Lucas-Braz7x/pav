from marshmallow import Schema, ValidationError, fields, validates, validate

class MedicalRecordResponseSchema(Schema):
    consultationId = fields.Int()
    diagnosis = fields.Str()
    id = fields.Int()
    notes = fields.Str()
    prescription = fields.Str()

class MedicalRecordListResponseSchema(Schema):
    medicalRecords = fields.List(fields.Nested(MedicalRecordResponseSchema))

class MedicalRecordRequestSchema(Schema):
    consultationId = fields.Int(required=False, validate=validate.Range(min=1))
    diagnosis = fields.Str(required=False)
    notes = fields.Str(required=False)
    prescription = fields.Str(required=False)

    @validates("diagnosis")
    def validate_diagnosis(self, value):
        if len(value) < 3:
            raise ValidationError("Diagnosis must be at least 3 characters long.")

    @validates("notes")
    def validate_notes(self, value):
        if len(value) < 10:
            raise ValidationError("Notes must be at least 10 characters long.")

    @validates("prescription")
    def validate_prescription(self, value):
        if len(value) < 5:
            raise ValidationError("Prescription must be at least 5 characters long.")