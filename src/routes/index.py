from src.controller.DocumentationController import DocumentationController
from src.controller.PatientController import PatientController
from src.controller.DoctorController import DoctorController
from src.controller.ConsultationController import ConsultationController
from src.controller.AppointmentController import AppointmentController
from src.controller.MedicalRecordController import MedicalRecordController

def initialize_routes(api):
    api.add_resource(PatientController, '/patients/name/<string:name>', endpoint='getByName')
    api.add_resource(PatientController, '/patients', '/patients/<int:patient_id>')
    api.add_resource(DoctorController, '/doctors', '/doctors/<int:doctor_id>')
    api.add_resource(DoctorController, '/doctors/name/<string:name>', endpoint='getByNameDoctor')
    api.add_resource(ConsultationController, '/consultations', '/consultations/<int:consultation_id>')
    api.add_resource(ConsultationController, '/consultations/doctorName/<string:doctorName>', endpoint='findByDoctorName')
    api.add_resource(AppointmentController, '/appointments/date/<string:date>', endpoint='getByDate')
    api.add_resource(AppointmentController, '/appointments', '/appointments/<int:appointment_id>')
    api.add_resource(MedicalRecordController, '/medical/record', '/medical/record/<int:medicalRecord_id>')
    api.add_resource(DocumentationController, '/documentation', resource_class_kwargs={'api': api})
