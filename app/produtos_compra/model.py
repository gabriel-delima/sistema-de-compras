from app.extensions import db
from app.association import association_carrinhos_produtos_compra , association_pedidos_produtos_compra

class ProdutosCompra(db.Model):
    __tablename__ = 'produtos_compra'
    id = db.Column(db.Integer, primary_key = True)
    quantidade = db.Column(db.Integer, nullable = False)
    valor_unitario = db.Column(db.Integer, nullable = False)
    valor_total = db.Column(db.Integer, nullable = False)

    # pedidos(many) <-> produtos_compra(many)
    pedidos = db.relationship('Pedidos', secondary=association_pedidos_produtos_compra , backref='pedido_produto_compra')

    # carrinhos(many) <-> produtos_compra(many)
    carrinhos = db.relationship('Carrinhos', secondary=association_carrinhos_produtos_compra , backref='carrinho_produto_compra')

    # produtos(one) <-> produtos_compra(many)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))

    def json(self):
        return{
            'quantidade':self.quantidade,
            'valor_unitario':self.valor_unitario,
            'valor_total':self.valor_total,
        }
