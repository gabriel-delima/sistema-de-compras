from app.extensions import db

association_pedidos_produtos_compra = db.Table('association_pedidos_produtos_compra',db.Model.metadata,
                                        db.Column('produtos_compra',db.Integer, db.ForeignKey('produtos_compra.id')),
                                        db.Column('pedidos',db.Integer,db.ForeignKey('pedidos.id')))

association_carrinhos_produtos_compra = db.Table('association_carrinhos_produtos_compra',db.Model.metadata,
                                        db.Column('produtos_compra',db.Integer, db.ForeignKey('produtos_compra.id')),
                                        db.Column('carrinhos',db.Integer,db.ForeignKey('carrinhos.id')))