from config.database import get_db

class ConsultaRepository:
    def salvar(self, consulta):
        db = get_db()
        db.execute(
            'INSERT INTO consultas (paciente_id, dentista_id, data) VALUES (?, ?, ?)',
            (consulta.paciente_id, consulta.dentista_id, consulta.data)
        )
        db.commit()
        db.close()

    def listar(self):
        db = get_db()
        dados = db.execute('SELECT * FROM consultas').fetchall()
        db.close()
        return dados
