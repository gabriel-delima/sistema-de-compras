from app.extensions import db

class ImagensProduto(db.Model):
    __tablename__ = 'imagens_produtos'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(100), nullable = False)
    descricao = db.Column(db.String(150), nullable = False)

    # imagens_produto(many) <-> produtos(one)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))

    def json(self):
        return{
            'url':self.url,
            'descricao':self.descricao
        }



class Produtos(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    descricao = db.Column(db.String(150), nullable = False)
    preco = db.Column(db.Integer, nullable = False)
    estoque = db.Column(db.Integer, nullable = False)

    # imagens_produto(many) <-> produtos(one)
    imagem_produto = db.relationship('ImagensProduto', backref = 'imagem_produto')

    # produtos(one) <-> produtos_compra(many)
    produto_compra = db.relationship('ProdutosCompra', backref = 'produto_compra')

    def json(self):
        return{
            'nome':self.nome,
            'descricao':self.descricao,
            'preco':self.preco,
            'estoque':self.estoque
        }