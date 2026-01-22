from config.database import get_db

class DentistaRepository:
    def salvar(self, dentista):
        db = get_db()
        db.execute(
            'INSERT INTO dentistas (nome, especialidade) VALUES (?, ?)',
            (dentista.nome, dentista.especialidade)
        )
        db.commit()
        db.close()

    def listar(self):
        db = get_db()
        dados = db.execute('SELECT * FROM dentistas').fetchall()
        db.close()
        return dados
