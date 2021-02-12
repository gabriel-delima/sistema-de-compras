from flask import request, jsonify, render_template
from flask.views import MethodView
from app.usuario.model import Usuarios
from app.extensions import db, mail
import bcrypt
from flask_mail import Message
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.usuario.auxiliar import testar_entradas_usuario

class UsuarioDetails(MethodView): #/usuarios
    def get(self):
        usuarios = Usuarios.query.all()
        return jsonify([usuario.json() for usuario in usuarios]),200
    def post(self):
        dados = request.json        
        nome = dados.get('nome')
        email = dados.get('email')
        senha = str(dados.get('senha'))
        cpf = dados.get('cpf')
        nascimento = dados.get('nascimento')
        carrinho_id = dados.get('carrinho_id')
        telefone = dados.get('telefone')
        telefone_opicional = dados.get('telefone_opicional')

        error = testar_entradas_usuario(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional)
        if (error != False):
            return error
        
        if Usuarios.query.filter_by(cpf = cpf ).first():
            return{"error":"CPF já cadastrado"}
        if Usuarios.query.filter_by(email = email ).first():
            return{"error":"E-mail já cadastrado"}

        senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())

        usuario = Usuarios(nome = nome, email = email, senha_hash = senha_hash , cpf = cpf, nascimento = nascimento, 
                            carrinho_id = carrinho_id, telefone = telefone, telefone_opicional = telefone_opicional)

        db.session.add(usuario)
        db.session.commit()

        msg = Message(sender = "gabriel.lima.moura@poli.ufrj.br",
                      recipients = [email],
                      subject = 'Cadastro Realizado - LACTAM',
                      html = render_template('email_cadastro.html', nome = nome))
        mail.send(msg)
        return usuario.json() , 200
        
# Método só pode ser acessado por usuários logados
class PaginaUsuario(MethodView):   #/usuarios/<int:id>
    decorators = [jwt_required]
    def get(self,id):
        if get_jwt_identity() != id:
            return {"error": "Usuário não permitido"}, 400
        usuario = Usuarios.query.get_or_404(id)
        return usuario.json(),200
    def put(self,id):
        if get_jwt_identity() != id:
            return {"error": "Usuário não permitido"}, 400
        usuario = Usuarios.query.get_or_404(id)
        dados = request.json        
        nome = dados.get('nome')
        email = dados.get('email')
        senha = str(dados.get('senha'))
        cpf = dados.get('cpf')
        nascimento = dados.get('nascimento')
        carrinho_id = dados.get('carrinho_id')
        telefone = dados.get('telefone')
        telefone_opicional = dados.get('telefone_opicional')

        error = testar_entradas_usuario(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional)
        if (error != False):
            return error

        if (usuario.cpf != cpf) and (Usuarios.query.filter_by(cpf = cpf ).first()):
            return{"error":"CPF já cadastrado"}
        if (usuario.email != email) and (Usuarios.query.filter_by(email = email ).first()):
            return{"error":"E-mail já cadastrado"}
        
        usuario.nome = nome
        usuario.email = email
        usuario.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
        usuario.cpf = cpf
        usuario.nascimento = nascimento
        usuario.telefone = telefone
        usuario.telefone_opicional = telefone_opicional
        usuario.carrinho_id = carrinho_id

        db.session.commit()
        return usuario.json() , 200

    def patch(self,id):
        if get_jwt_identity() != id:
            return {"error": "Usuário não permitido"}, 400
        usuario = Usuarios.query.get_or_404(id)
        dados = request.json        
        nome = dados.get('nome', usuario.nome)
        email = dados.get('email', usuario.email)
        cpf = dados.get('cpf', usuario.cpf)
        nascimento = dados.get('nascimento', usuario.nascimento)
        telefone = dados.get('telefone', usuario.telefone)
        telefone_opicional = dados.get('telefone_opicional', usuario.telefone_opicional)
        carrinho_id = dados.get('carrinho_id',usuario.carrinho_id)
        
        senha = (dados.get('senha'))
        if senha == None:
            senha = "123456" #recebe isso somente para a funcao testar_entradas_usuario não retornar nenhum erro relacionado à senha
            print("entrwi na opcao  1")
            error = testar_entradas_usuario(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional)
            if (error != False):
                return error
            
            if (usuario.cpf != cpf) and (Usuarios.query.filter_by(cpf = cpf ).first()):
                return{"error":"CPF já cadastrado"}
            if (usuario.email != email) and (Usuarios.query.filter_by(email = email ).first()):
                return{"error":"E-mail já cadastrado"}
            
            usuario.nome = nome
            usuario.email = email
            usuario.cpf = cpf
            usuario.nascimento = nascimento
            usuario.telefone = telefone
            usuario.telefone_opicional = telefone_opicional
            usuario.carrinho_id = carrinho_id 

            db.session.commit()
            return usuario.json() , 200
        else:
            senha = str(senha)
            print("entrwi na opcao  2")
            error = testar_entradas_usuario(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional)
            if (error != False):
                return error
            
            if (usuario.cpf != cpf) and (Usuarios.query.filter_by(cpf = cpf ).first()):
                return{"error":"CPF já cadastrado"}
            if (usuario.email != email) and (Usuarios.query.filter_by(email = email ).first()):
                return{"error":"E-mail já cadastrado"}
            
            usuario.nome = nome
            usuario.email = email
            usuario.senha_hash = bcrypt.hashpw(senha.encode(),bcrypt.gensalt())
            usuario.cpf = cpf
            usuario.nascimento = nascimento
            usuario.telefone = telefone
            usuario.telefone_opicional = telefone_opicional
            usuario.carrinho_id = carrinho_id 

            db.session.commit()
            return usuario.json() , 200
    def delete(self,id):
        if get_jwt_identity() != id:
            return {"error": "Usuário não permitido"}, 400
        usuario = Usuarios.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario.json(), 200

class UsuarioLogin(MethodView):   #/usuarios/login
    def post(self):
        dados = request.json
        email = dados.get('email')
        senha = str(dados.get('senha'))
        
        usuario = Usuarios.query.filter_by(email=email).first()

        if not usuario :
            return {"error":"E-mail não cadastrado"}, 400

        if not bcrypt.checkpw(senha.encode(), usuario.senha_hash):
            return {"error":"Senha Inválida"}, 400

        token = create_access_token(identity = usuario.id)

        return {"token":token}, 200