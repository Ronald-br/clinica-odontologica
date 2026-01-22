import sqlite3

def get_db():
    return sqlite3.connect('database.db')

def create_tables():
    db = get_db()
    c = db.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS pacientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, telefone TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS dentistas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, especialidade TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS consultas (id INTEGER PRIMARY KEY AUTOINCREMENT, paciente_id INTEGER, dentista_id INTEGER, data TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS pagamentos (id INTEGER PRIMARY KEY AUTOINCREMENT, consulta_id INTEGER, valor REAL)')

    db.commit()
    db.close()
