from flask import  request, jsonify
from flask.views import MethodView
from app.produtos_compra.model import  ProdutosCompra
from app.extensions import db
from app.produtos_compra.auxiliar import testar_entradas_produto_compra

class ProdutosCompraDetails(MethodView): # /produtos_compra
    def get(self):
        produtos_compra = ProdutosCompra.query.all()
        return jsonify([produto_compra.json() for produto_compra in produtos_compra]),200
    
    def post(self):
        dados = request.json
        quantidade = dados.get("quantidade")
        valor_unitario = dados.get("valor_unitario")
        produto_id = dados.get("produto_id")

        error = testar_entradas_produto_compra(quantidade,valor_unitario,produto_id)
        if (error != False):
            return error

        valor_total = quantidade * valor_unitario

        produto_compra  = ProdutosCompra(quantidade = quantidade , valor_unitario = valor_unitario, valor_total = valor_total, produto_id = produto_id)

        db.session.add(produto_compra)
        db.session.commit()

        return produto_compra.json(), 200

class PaginaProdutosCompra(MethodView): # /produtos_compra/<int:id>
    def get(self,id):
        produto_compra = ProdutosCompra.query.get_or_404(id)
        return produto_compra.json(), 200

    def put(self,id):
        produto_compra = ProdutosCompra.query.get_or_404(id)
        dados = request.json
        quantidade = dados.get("quantidade")
        valor_unitario = dados.get("valor_unitario")
        produto_id = dados.get("produto_id")

        error = testar_entradas_produto_compra(quantidade,valor_unitario,produto_id)
        if (error != False):
            return error

        valor_total = quantidade * valor_unitario

        produto_compra.quantidade = quantidade
        produto_compra.valor_unitario = valor_unitario
        produto_compra.valor_total = valor_total
        produto_compra.produto_id = produto_id

        db.session.commit()
        return produto_compra.json() , 200

    def patch(self,id):
        produto_compra = ProdutosCompra.query.get_or_404(id)
        dados = request.json
        quantidade = dados.get("quantidade", produto_compra.quantidade)
        valor_unitario = dados.get("valor_unitario", produto_compra.valor_unitario)
        produto_id = dados.get("produto_id", produto_compra.produto_id)

        error = testar_entradas_produto_compra(quantidade,valor_unitario,produto_id)
        if (error != False):
            return error
        
        valor_total = quantidade * valor_unitario

        produto_compra.quantidade = quantidade
        produto_compra.valor_unitario = valor_unitario
        produto_compra.valor_total = valor_total
        produto_compra.produto_id = produto_id

        db.session.commit()
        return produto_compra.json() , 200

    def delete(self,id):
        produto_compra = ProdutosCompra.query.get_or_404(id)
        db.session.delete(produto_compra)
        db.session.commit()
        return produto_compra.json(), 200
        