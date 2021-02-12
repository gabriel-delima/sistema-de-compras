from app.extensions import db

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    senha_hash = db.Column(db.String(200), nullable = False)
    cpf = db.Column(db.Integer, unique = True, nullable = False)
    nascimento = db.Column(db.String(10), nullable = False)
    telefone = db.Column(db.Integer, nullable = False)
    telefone_opicional = db.Column(db.Integer, nullable=True)

    # enderecos(many) <-> usuarios(one) 
    endereco = db.relationship('Enderecos', backref = 'endereco_usuario')
    
    # pedidos(many) <-> usuarios(one)
    pedido = db.relationship('Pedidos', backref = 'pedido_usuario')

    # carrinhos(one) <-> usuarios(one)
    carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinhos.id'))
    
    def json(self):
        return{
            'nome':self.nome,
#            'email':self.email,
#            'cpf':self.cpf,
#            'nascimento':self.nascimento,
#            'telefone':self.telefone,
#            'telefone_opicional':self.telefone_opicional,
            'carrinho_id':self.carrinho_id
        }