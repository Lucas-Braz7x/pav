# Requisitos

## Patients

- O sistema deve permitir o cadastro de pacientes com nome, idade e histórico médico.
- O sistema deve listar todos os pacientes cadastrados.
- O sistema deve validar que a idade do paciente é um valor positivo.
- O sistema deve validar o tamanho do cpf.
- O sistema deve validar se o cpf já existe.
- Pesquisa de Consultas por Paciente: O sistema deve permitir que os usuários pesquisem e filtrem consultas com base no nome do paciente.

## Doctor

- O sistema deve permitir o cadastro de médicos com nome, especialidade e CRM.
- O sistema deve listar todos os médicos cadastrados.
- O sistema deve validar listar todos os médicos cadastrados.
- O sistema deve validar se o crm é maior que 0.
- O sistema deve validar se o crm já existe.
- Pesquisa de Consultas por Médico: O sistema deve permitir que os usuários pesquisem e filtrem consultas com base no nome do médico.

# Consultation

- O sistema deve permitir agendar consultas entre pacientes e médicos.
- O sistema deve listar todas as consultas agendadas.
- O sistema deve verificar se existe o médico e o paciente cadastrados
- O sistema deve fornecer relatórios que exibam as consultas realizadas em um dia
- O sistema deve trazer o Medical Record da Consultation, caso exista
- O Sistema só deve permitir consulta se existir um médico e um paciente

# Agendamento

- O sistema deve permitir cancelar consultas agendadas.
- O sistema deve cadastra agendamentos junto com a consulta

# MedicalRecord

- O sistema não deve cadastrar um MedicalRecord senão existir uma consulta
- O sistema só deve permitir um MedicalRecord por consulta
