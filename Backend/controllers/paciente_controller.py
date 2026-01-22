from flask import Blueprint, request, jsonify
from models.paciente import Paciente
from services.paciente_service import PacienteService

paciente_bp = Blueprint('paciente', __name__)
service = PacienteService()

@paciente_bp.route('/pacientes', methods=['POST'])
def cadastrar():
    data = request.json
    paciente = Paciente(data['nome'], data['telefone'])
    service.cadastrar(paciente)
    return '', 201

@paciente_bp.route('/pacientes', methods=['GET'])
def listar():
    dados = service.listar()
    return jsonify(dados)
