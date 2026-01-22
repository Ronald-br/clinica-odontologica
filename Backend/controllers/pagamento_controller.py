from flask import Blueprint, request, jsonify
from models.pagamento import Pagamento
from services.pagamento_service import PagamentoService

pagamento_bp = Blueprint('pagamento', __name__)
service = PagamentoService()

@pagamento_bp.route('/pagamentos', methods=['POST'])
def cadastrar():
    data = request.json
    pagamento = Pagamento(data['consulta_id'], data['valor'])
    service.cadastrar(pagamento)
    return '', 201

@pagamento_bp.route('/pagamentos', methods=['GET'])
def listar():
    dados = service.listar()
    return jsonify(dados)
