from flask import Flask
from flask_cors import CORS
from config.database import create_tables
from controllers.paciente_controller import paciente_bp
from controllers.dentista_controller import dentista_bp
from controllers.consulta_controller import consulta_bp
from controllers.pagamento_controller import pagamento_bp

app = Flask(__name__)
CORS(app)

create_tables()

app.register_blueprint(paciente_bp)
app.register_blueprint(dentista_bp)
app.register_blueprint(consulta_bp)
app.register_blueprint(pagamento_bp)

app.run(debug=True)
