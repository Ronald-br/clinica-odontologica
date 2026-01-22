from repositories.pagamento_repository import PagamentoRepository

class PagamentoService:
    def __init__(self):
        self.repo = PagamentoRepository()

    def cadastrar(self, pagamento):
        self.repo.salvar(pagamento)

    def listar(self):
        return self.repo.listar()
