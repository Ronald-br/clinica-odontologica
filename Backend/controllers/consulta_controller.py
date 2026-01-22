from flask import Blueprint, request, jsonify
from models.consulta import Consulta
from services.consulta_service import ConsultaService

consulta_bp = Blueprint('consulta', __name__)
service = ConsultaService()

@consulta_bp.route('/consultas', methods=['POST'])
def cadastrar():
    data = request.json
    consulta = Consulta(data['paciente_id'], data['dentista_id'], data['data'])
    service.cadastrar(consulta)
    return '', 201

@consulta_bp.route('/consultas', methods=['GET'])
def listar():
    dados = service.listar()
    return jsonify(dados)
