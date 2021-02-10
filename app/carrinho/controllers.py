from flask import  request, Blueprint, jsonify
from app.carrinho.model import Carrinhos
from app.extensions import db


def testar_entradas(valor_frete,valor_total,usuario_id):
    if ( not(isinstance(valor_frete,int)) or 
         not(isinstance(valor_total,int)) ):

        return{"error":"Algum tipo inválido"},400
        
    if ((valor_frete < 0) or 
        (valor_total < 0)):

        return{"error":"Os valores devem ser maiores que 0"},400
        
    if (usuario_id != None) and (not(isinstance(usuario_id,int)) or (usuario_id<0)) :
        return{"error": "usuario_id deve ser inteiro positivo"}
    return False


carrinho_api = Blueprint('carrinho_api', __name__)

@carrinho_api.route('/carrinhos',methods = ['GET','POST'])
def index():
    if request.method == "GET":
        carrinhos = Carrinhos.query.all()
        return jsonify([carrinho.json() for carrinho in carrinhos]),200

    if request.method == "POST":
        dados = request.json        
        valor_frete = dados.get('valor_frete')
        valor_total = dados.get('valor_total')
        usuario_id = dados.get('usuario_id')
        
        if valor_frete == None:
            valor_frete = 0
        if valor_total == None:
            valor_total = 0

        error = testar_entradas(valor_frete,valor_total,usuario_id)
        if (error != False):
            return error
        
        carrinho = Carrinhos(valor_frete = valor_frete, valor_total = valor_total, usuario_id = usuario_id)

        db.session.add(carrinho)
        db.session.commit()

        return carrinho.json() , 200

@carrinho_api.route('/carrinhos/<int:id>',methods = ['GET','PUT','PATCH','DELETE'])
def pagina_carrinho(id):

    carrinho = Carrinhos.query.get_or_404(id)

    if request.method == "GET":
        return carrinho.json(),200
    
    if request.method =='PUT':
        dados = request.json      
        valor_frete = dados.get('valor_frete')
        valor_total = dados.get('valor_total')
        usuario_id = dados.get('usuario_id')
        
        if valor_frete == None:
            valor_frete = 0
        if valor_total == None:
            valor_total = 0
        error = testar_entradas(valor_frete,valor_total)
        if (error != False):
            return error
        
        carrinho.valor_frete = valor_frete
        carrinho.valor_total = valor_total
        carrinho.usuario_id = usuario_id
        
        db.session.commit()
        return carrinho.json() , 200

    if request.method == "PATCH":
        dados = request.json        

        valor_frete = dados.get('valor_frete', carrinho.valor_frete)
        valor_total = dados.get('valor_total', carrinho.valor_total)
        usuario_id = dados.get('usuario_id', carrinho.usuario_id)

        error = testar_entradas(valor_frete,valor_total,usuario_id)
        if (error != False):
            return error

        carrinho.valor_frete = valor_frete
        carrinho.valor_total = valor_total
        carrinho.usuario_id = usuario_id

        db.session.commit()
        return carrinho.json() , 200
    
    if request.method =='DELETE':
        db.session.delete(carrinho)
        db.session.commit()
        return carrinho.json(), 200