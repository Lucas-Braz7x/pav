from flask_restful import  Resource

class DocumentationController(Resource):
    def get(self):
        return '''
        <h1>api documentation</h1>
        <ul>
            <h1>API Documentation</h1>
            <li><strong>GET /patients</strong> - List all patients</li>
            <li><strong>POST /patients</strong> - Create a new patient</li>
            <li><strong>GET /patients/&lt;patient_id&gt;</strong> - Get information about a specific patient</li>
            <li><strong>PUT /patients/&lt;patient_id&gt;</strong> - Update information about a specific patient</li>
            <li><strong>DELETE /patients/&lt;patient_id&gt;</strong> - Delete a specific patient</li>
            <li><strong>GET /doctors</strong> - List all doctors</li>
            <li><strong>POST /doctors</strong> - Create a new doctor</li>
            <li><strong>GET /doctors/&lt;doctor_id&gt;</strong> - Get information about a specific doctor</li>
            <li><strong>PUT /doctors/&lt;doctor_id&gt;</strong> - Update information about a specific doctor</li>
            <li><strong>DELETE /doctors/&lt;doctor_id&gt;</strong> - Delete a specific doctor</li>
            <li><strong>GET /consultations</strong> - List all consultations</li>
            <li><strong>POST /consultations</strong> - Create a new consultation</li>
            <li><strong>GET /consultations/&lt;consultation_id&gt;</strong> - Get information about a specific consultation</li>
            <li><strong>PUT /consultations/&lt;consultation_id&gt;</strong> - Update information about a specific consultation</li>
            <li><strong>DELETE /consultations/&lt;consultation_id&gt;</strong> - Delete a specific consultation</li>
            <li><strong>GET /documentation</strong> - View API documentation</li>
        </ul>
        '''
    