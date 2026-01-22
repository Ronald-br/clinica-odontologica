from repositories.consulta_repository import ConsultaRepository

class ConsultaService:
    def __init__(self):
        self.repo = ConsultaRepository()

    def cadastrar(self, consulta):
        self.repo.salvar(consulta)

    def listar(self):
        return self.repo.listar()
