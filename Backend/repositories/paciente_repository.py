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

    def listar(self, nome=''):
        db = get_db()
        if nome:
            dados = db.execute(
                'SELECT * FROM pacientes WHERE nome LIKE ?',
                (f'%{nome}%',)
            ).fetchall()
        else:
            dados = db.execute('SELECT * FROM pacientes').fetchall()
        db.close()
        return dados