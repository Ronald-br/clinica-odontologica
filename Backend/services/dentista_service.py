from repositories.dentista_repository import DentistaRepository

class DentistaService:
    def __init__(self):
        self.repo = DentistaRepository()

    def cadastrar(self, dentista):
        self.repo.salvar(dentista)

    def listar(self):
        return self.repo.listar()
