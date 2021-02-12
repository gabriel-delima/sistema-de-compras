from flask import  request, jsonify
from flask.views import MethodView
from app.carrinho.model import Carrinhos
from app.extensions import db
from app.carrinho.auxiliar import testar_entradas_carrinho


class CarrinhoDetails(MethodView):      # /carrinhos
    def get(self):
        carrinhos = Carrinhos.query.all()
        return jsonify([carrinho.json() for carrinho in carrinhos]),200

    def post(self):
        dados = request.json        
        valor_frete = dados.get('valor_frete')
        valor_total = dados.get('valor_total')
        usuario_id = dados.get('usuario_id')
        
        if valor_frete == None:
            valor_frete = 0
        if valor_total == None:
            valor_total = 0

        error = testar_entradas_carrinho(valor_frete,valor_total,usuario_id)
        if (error != False):
            return error
        
        carrinho = Carrinhos(valor_frete = valor_frete, valor_total = valor_total, usuario_id = usuario_id)

        db.session.add(carrinho)
        db.session.commit()

        return carrinho.json() , 200

class PaginaCarrinhos(MethodView):      # /carrinhos/<int:id>
    def get(self,id):
        carrinho = Carrinhos.query.get_or_404(id)
        return carrinho.json(),200

    def put(self,id):
        carrinho = Carrinhos.query.get_or_404(id)
        dados = request.json      
        valor_frete = dados.get('valor_frete')
        valor_total = dados.get('valor_total')
        usuario_id = dados.get('usuario_id')
        
        if valor_frete == None:
            valor_frete = 0
        if valor_total == None:
            valor_total = 0
        error = testar_entradas_carrinho(valor_frete,valor_total,usuario_id)
        if (error != False):
            return error
        
        carrinho.valor_frete = valor_frete
        carrinho.valor_total = valor_total
        carrinho.usuario_id = usuario_id
        
        db.session.commit()
        return carrinho.json() , 200

    def patch(self,id):
        carrinho = Carrinhos.query.get_or_404(id)
        dados = request.json        

        valor_frete = dados.get('valor_frete', carrinho.valor_frete)
        valor_total = dados.get('valor_total', carrinho.valor_total)
        usuario_id = dados.get('usuario_id', carrinho.usuario_id)

        error = testar_entradas_carrinho(valor_frete,valor_total,usuario_id)
        if (error != False):
            return error

        carrinho.valor_frete = valor_frete
        carrinho.valor_total = valor_total
        carrinho.usuario_id = usuario_id

        db.session.commit()
        return carrinho.json() , 200

    def delete(self,id):
        carrinho = Carrinhos.query.get_or_404(id)
        db.session.delete(carrinho)
        db.session.commit()
        return carrinho.json(), 200

