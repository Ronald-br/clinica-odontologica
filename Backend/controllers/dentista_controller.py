from flask import Blueprint, request, jsonify
from models.dentista import Dentista
from services.dentista_service import DentistaService

dentista_bp = Blueprint('dentista', __name__)
service = DentistaService()

@dentista_bp.route('/dentistas', methods=['POST'])
def cadastrar():
    data = request.json
    dentista = Dentista(data['nome'], data['especialidade'])
    service.cadastrar(dentista)
    return '', 201

@dentista_bp.route('/dentistas', methods=['GET'])
def listar():
    dados = service.listar()
    return jsonify(dados)
