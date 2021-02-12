from app.extensions import db

class Enderecos(db.Model):
    __tablename__ = 'enderecos'
    id = db.Column(db.Integer, primary_key = True)
    cep = db.Column(db.Integer, nullable = False)
    logadouro = db.Column(db.String(50), nullable = False)
    numero = db.Column(db.Integer, nullable = False)
    complemento = db.Column(db.String(100), nullable = True)
    bairro = db.Column(db.String(50), nullable = False)
    cidade = db.Column(db.String(50), nullable = False)
    estado = db.Column(db.String(50), nullable = False) 

    # enderecos(many) <-> usuarios(one)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    
    def json(self):
        return{
            'cep':self.cep,
            'logadouro':self.logadouro,
            'numero':self.numero,
            'complemento':self.complemento,
            'bairro':self.bairro,
            'cidade':self.cidade,
            'estado':self.estado,
            'usuario_id':self.usuario_id
        }
