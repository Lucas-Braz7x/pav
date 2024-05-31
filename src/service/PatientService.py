from src.repository.PatientRepository import PatientRepository
from src.view.ModelView import ModelView
from flask_restful import abort, request

class PatientService:
    def __init__(self):
        self.patientRepository = PatientRepository()
        self.patientView = ModelView()

    def validation(self, data):
        name = data.get('name')
        cpf = data.get('cpf')
        age = data.get('age')

        if not name or not cpf or not age:
            abort(400, message="Name, CPF, and age are required")

        if len(cpf) != 11:
            abort(400, message="cpf length is not valid")

        if(age < 0): 
            abort(400, message="age is not valid")

    def validationExistCpf(self, data, patient_id=None):
        cpf = data.get('cpf')
        patients = self.patientRepository.getAll()

        request_method = request.method

        filtered_patients = []
        
        if(request_method == "PUT" and patient_id):
            patientRecord = self.patientRepository.getById(patient_id)
            if(patientRecord.cpf != cpf):
                filtered_patients = [patient for patient in patients if patient.cpf == cpf]
        else:
            filtered_patients = [patient for patient in patients if patient.cpf == cpf]
            print(filtered_patients)


        if(len(filtered_patients) > 0):
            abort(400, message=f'cpf {cpf} already exist in database')

        return cpf


    def find(self, patient_id=None):
        if patient_id:
            return self.patientRepository.getById(patient_id)
        
        return self.patientRepository.getAll()
        
    
    def findByName(self, name=None):
        if name:
            return self.patientRepository.getByName(name)
        
        abort(400, message="name is not valid")
    
    def create(self, data):
        self.validation(data) 
        self.validationExistCpf(data)     
            
        return self.patientRepository.create(data)

    def update(self, patient_id, data):
        self.validation(data)
        self.validationExistCpf(data=data, patient_id=patient_id)     

        updated_patient = self.patientRepository.update(patient_id, data)
        
        return self.patientView.formatter(updated_patient)

    def delete(self, patient_id):
        print("CHAmou deleted")
        self.patientRepository.delete(patient_id)
        return self.patientView.registerIdDeleted("Patient deleted")
