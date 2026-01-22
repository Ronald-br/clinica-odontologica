from repositories.paciente_repository import PacienteRepository

class PacienteService:
    def __init__(self):
        self.repo = PacienteRepository()

    def cadastrar(self, paciente):
        self.repo.salvar(paciente)

    def listar(self):
        return self.repo.listar()
