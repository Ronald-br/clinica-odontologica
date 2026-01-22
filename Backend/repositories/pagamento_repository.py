from config.database import get_db

class PagamentoRepository:
    def salvar(self, pagamento):
        db = get_db()
        db.execute(
            'INSERT INTO pagamentos (consulta_id, valor) VALUES (?, ?)',
            (pagamento.consulta_id, pagamento.valor)
        )
        db.commit()
        db.close()

    def listar(self):
        db = get_db()
        dados = db.execute('SELECT * FROM pagamentos').fetchall()
        db.close()
        return dados
