from app.extensions import db
from app.association import association_carrinhos_produtos_compra


class Carrinhos(db.Model):
    __tablename__ = 'carrinhos'
    id = db.Column(db.Integer, primary_key = True)
    valor_frete = db.Column(db.Integer, nullable = False)
    valor_total = db.Column(db.Integer, nullable = False)

    # carrinhos(many) <-> produtos_compra(many)
    produtos_compra = db.relationship('ProdutosCompra', secondary=association_carrinhos_produtos_compra , backref='produto_compra_carrinho')

    # carrinhos(one) <-> usuarios(one)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    

    def json(self):
        return{
            'valor_frete':self.valor_frete,
            'valor_total':self.valor_total,
            'usuario_id':self.usuario_id
        }
