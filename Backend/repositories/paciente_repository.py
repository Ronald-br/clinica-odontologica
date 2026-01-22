from config.database import get_db

class PacienteRepository:
    def salvar(self, paciente):
        db = get_db()
        db.execute(
            'INSERT INTO pacientes (nome, telefone) VALUES (?, ?)',
            (paciente.nome, paciente.telefone)
        )
        db.commit()
        db.close()

    def listar(self):
        db = get_db()
        dados = db.execute('SELECT * FROM pacientes').fetchall()
        db.close()
        return dados
