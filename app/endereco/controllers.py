from flask import  request, jsonify
from flask.views import MethodView
from app.endereco.model import Enderecos
from app.extensions import db
from app.endereco.auxiliar import testar_entradas_endereco


class EnderecoDetails(MethodView):      # /enderecos
    def get(self):
        enderecos = Enderecos.query.all()
        return jsonify([endereco.json() for endereco in enderecos]),200

    def post(self):
        dados = request.json        
        cep = dados.get('cep')
        logadouro = dados.get('logadouro')
        numero = dados.get('numero')
        complemento = dados.get('complemento')
        bairro = dados.get('bairro')
        cidade = dados.get('cidade')
        estado = dados.get('estado')
        usuario_id = dados.get("usuario_id")
        
        error = testar_entradas_endereco(cep,logadouro,numero,complemento,bairro,cidade,estado,usuario_id)
        if (error != False):
            return error
        
        endereco = Enderecos(cep = cep, logadouro = logadouro, numero = numero, complemento = complemento, 
                             bairro = bairro, cidade = cidade, estado = estado, usuario_id = usuario_id)

        db.session.add(endereco)
        db.session.commit()

        return endereco.json() , 200

class PaginaEnderecos(MethodView):      # /enderecos/<int:id>
    def get(self,id):
        endereco = Enderecos.query.get_or_404(id)
        return endereco.json(),200

    def put(self,id):
        endereco = Enderecos.query.get_or_404(id)
        dados = request.json      
        cep = dados.get('cep')
        logadouro = dados.get('logadouro')
        numero = dados.get('numero')
        complemento = dados.get('complemento')
        bairro = dados.get('bairro')
        cidade = dados.get('cidade')
        estado = dados.get('estado')
        usuario_id = dados.get("usuario_id")
        
        error = testar_entradas_endereco(cep,logadouro,numero,complemento,bairro,cidade,estado,usuario_id)
        if (error != False):
            return error
        
        endereco.cep = cep
        endereco.logadouro = logadouro
        endereco.numero = numero
        endereco.complemento = complemento
        endereco.bairro = bairro
        endereco.cidade = cidade
        endereco.estado = estado
        endereco.usuario_id = usuario_id
        
        db.session.commit()
        return endereco.json() , 200

    def patch(self,id):
        endereco = Enderecos.query.get_or_404(id)
        dados = request.json        
        cep = dados.get('cep', endereco.cep)
        logadouro = dados.get('logadouro', endereco.logadouro)
        numero = dados.get('numero',endereco.numero)
        complemento = dados.get('complemento',endereco.complemento)
        bairro = dados.get('bairro',endereco.bairro)
        cidade = dados.get('cidade',endereco.cidade)
        estado = dados.get('estado',endereco.estado)
        usuario_id = dados.get("usuario_id",endereco.usuario_id)

        error = testar_entradas_endereco(cep,logadouro,numero,complemento,bairro,cidade,estado,usuario_id)
        if (error != False):
            return error

        endereco.cep = cep
        endereco.logadouro = logadouro
        endereco.numero = numero
        endereco.complemento = complemento
        endereco.bairro = bairro
        endereco.cidade = cidade
        endereco.estado = estado
        endereco.usuario_id = usuario_id

        db.session.commit()
        return endereco.json() , 200

    def delete(self,id):
        endereco = Enderecos.query.get_or_404(id)
        db.session.delete(endereco)
        db.session.commit()
        return endereco.json(), 200

