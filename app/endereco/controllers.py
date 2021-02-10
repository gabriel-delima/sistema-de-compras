from flask import  request, Blueprint, jsonify
from app.endereco.model import Enderecos
from app.extensions import db


def testar_entradas(cep,logadouro,complemento,bairro,cidade,estado):
    #testes
    return False


endereco_api = Blueprint('endereco_api', __name__)

@endereco_api.route('/enderecos',methods = ['GET','POST'])
def index():
    if request.method == "GET":
        enderecos = Enderecos.query.all()
        return jsonify([endereco.json() for endereco in enderecos]),200

    if request.method == "POST":
        dados = request.json        
        cep = dados.get('cep')
        logadouro = dados.get('logadouro')
        complemento = dados.get('complemento')
        bairro = dados.get('bairro')
        cidade = dados.get('cidade')
        estado = dados.get('estado')
        
        error = testar_entradas(cep,logadouro,complemento,bairro,cidade,estado)
        if (error != False):
            return error
        
        endereco = Enderecos(cep = cep, logadouro = logadouro, complemento = complemento, 
                             bairro = bairro, cidade = cidade, estado = estado)

        db.session.add(endereco)
        db.session.commit()

        return endereco.json() , 200

@endereco_api.route('/enderecos/<int:id>',methods = ['GET','PUT','PATCH','DELETE'])
def pagina_endereco(id):

    endereco = Enderecos.query.get_or_404(id)

    if request.method == "GET":
        return endereco.json(),200
    
    if request.method =='PUT':
        dados = request.json      
        cep = dados.get('cep')
        logadouro = dados.get('logadouro')
        complemento = dados.get('complemento')
        bairro = dados.get('bairro')
        cidade = dados.get('cidade')
        estado = dados.get('estado')
        
        error = testar_entradas(cep,logadouro,complemento,bairro,cidade,estado)
        if (error != False):
            return error
        
        endereco.cep = cep
        endereco.logadouro = logadouro
        endereco.complemento = complemento
        endereco.bairro = bairro
        endereco.cidade = cidade
        endereco.estado = estado
        
        db.session.commit()
        return endereco.json() , 200

    if request.method == "PATCH":
        dados = request.json        

        valor_frete = dados.get('valor_frete', carrinho.valor_frete)
        valor_total = dados.get('valor_total', carrinho.valor_total)
        usuario_id = dados.get('usuario_id', carrinho.usuario_id)

        error = testar_entradas(cep,logadouro,complemento,bairro,cidade,estado)
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