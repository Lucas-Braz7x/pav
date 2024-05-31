from src.repository.DoctorRepository import DoctorRepository
from src.view.ModelView import ModelView
from flask_restful import abort, request

class DoctorService:
    def __init__(self):
        self.doctorRepository = DoctorRepository()
        self.doctorView = ModelView()

    def validation(self, data, doctorId=None):
        name = data.get('name')
        specialty = data.get('specialty')
        crm = data.get('crm')
        
        if not name or not specialty or not crm:
            abort(400, message="Name, specialty, and CRM are required")
        
        if crm <= 0: 
            abort(400, message="crm is not valid")

        doctors = self.doctorRepository.getAll()

        request_method = request.method

        filteredDoctors = []
        
        if(request_method == "PUT" and doctorId):
            doctorRecord = self.doctorRepository.getById(doctorId)
            if(doctorRecord.crm != str(crm)):
                filteredDoctors = [doctor for doctor in doctors if doctor.crm == str(crm)]
        else:
            filteredDoctors = [doctor for doctor in doctors if doctor.crm == str(crm)]

        if(len(filteredDoctors) > 0):
                abort(400, message="crm already exist in database")
        

    def find(self, doctor_id=None):
        if doctor_id:
            doctor = self.doctorRepository.getById(doctor_id)
            return self.doctorView.formatter(doctor)
        
        doctors = self.doctorRepository.getAll()
        return self.doctorView.formatterAll(doctors)
    
    def findByName(self, name=None):
        doctors = self.doctorRepository.getByName(name)
        return self.doctorView.formatterAll(doctors)
    
    def create(self, data):  
        self.validation(data)
        
        new_doctor = self.doctorRepository.create(data)
        
        return self.doctorView.formatter(new_doctor, "Doctor created")
        

    def update(self, doctor_id, data):
        self.validation(data, doctorId=doctor_id)

        updated_doctor = self.doctorRepository.update(doctor_id, data)
        
        return self.doctorView.formatter(updated_doctor, "Doctor updated")
        

    def delete(self, doctor_id):
        self.doctorRepository.delete(doctor_id)
        return self.doctorView.registerIdDeleted("Doctor deleted")
