from app.extensions import db
from app.association import association_pedidos_produtos_compra


class Pedidos(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key = True)
    
    data = db.Column(db.Date, nullable = False)
    #forma_pagamento = ...
    pagamento_aprovado = db.Column(db.Boolean, nullable = False)
    valor_frete = db.Column(db.Integer, primary_key = True)
    valor_total = db.Column(db.Integer, primary_key = True)

    # pedidos(many) <-> produtos_compra(many)
    produtos_compra = db.relationship('ProdutosCompra', secondary=association_pedidos_produtos_compra , backref='produto_compra_pedido')

    # pedidos(many) <-> usuarios(one)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    
    # endereco(many) <-> pedido(one) : endereco de entrega
    endereco_entrega_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'))

    # endereco(many) <-> pedido(one) : endereco de cobranca
    endereco_cobranca_id = db.Column(db.Integer, db.ForeignKey('enderecos.id'))

    def json(self):
        return{
            'quantidade':self.quantidade,
            'data':self.data,
            'pagamento_aprovado':self.pagamento_aprovado,
            'valor_frete':self.valor_frete,
            'valor_total':self.valor_total,
            'produto_id':self.produto_id,
            'usuario_id':self.usuario_id,
            'endereco_entrega_id':self.endereco_entrega_id,
            'endereco_cobranca_id':self.endereco_cobranca_id
        }
