from flask import  request, Blueprint, jsonify
from app.usuario.model import Usuarios
from app.extensions import db


def testar_entradas(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional):
    if nome is None:
        return{"error":"Nome Obrigatório"},400
    if email is None:
        return{"error":"Email Obrigatório"},400
    if senha is None:
        return{"error":"Senha Obrigatória"},400
    if cpf is None:
        return{"error":"CPF Obrigatório"},400
    if nascimento is None:
        return{"error":"Nascimento Obrigatório"},400
    if telefone is None:
        return{"error":"Telefone principal Obrigatório"},400

    if (not(isinstance(nome,str)) or 
        not(isinstance(email,str)) or 
        not(isinstance(senha,str)) or
        not(isinstance(cpf,int)) or 
        not(isinstance(nascimento,str)) or
        not(isinstance(telefone,int)) or 
        (telefone_opicional != None and not(isinstance(telefone_opicional,int)))):
        
        return{"error":"Algum tipo inválido"},400
        
    if (carrinho_id != None) and (not(isinstance(carrinho_id,int)) or (carrinho_id<0)) :
        return{"error": "carrinho_id deve ser inteiro positivo"}
    if len(nome) > 50:
        return{"error":"Nome deve conter até 50 caracteres"},400
    if len(email) > 50:
        return{"error":"E-mail deve conter até 50 caracteres"},400
    if len(senha) > 20:
        return{"error":"Senha deve conter até 20 caracteres"},400
    if len(str(cpf)) != 11:
        return{"error":"CPF deve conter 11 dígitos"},400
    if (len(nascimento) != 10):
        return{"error":"Nascimento deve estar no formato xx/xx/xxxx"},400
    if (nascimento[2] != "/") or (nascimento[2] != "/") or (nascimento[2] != "/"):
        return{"error":"Nascimento deve estar no formato xx/xx/xxxx"},400

    return False
    #validar cpf
    #validar email

usuario_api = Blueprint('usuario_api', __name__)

@usuario_api.route('/usuarios',methods = ['GET','POST'])
def index():
    if request.method == "GET":
        usuarios = Usuarios.query.all()
        return jsonify([usuario.json() for usuario in usuarios]),200

    if request.method == "POST":
        dados = request.json        
        nome = dados.get('nome')
        email = dados.get('email')
        senha = dados.get('senha') 
        cpf = dados.get('cpf')
        nascimento = dados.get('nascimento')
        carrinho_id = dados.get('carrinho_id')
        telefone = dados.get('telefone')
        telefone_opicional = dados.get('telefone_opicional')

        error = testar_entradas(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional)
        if (error != False):
            return error
        
        if Usuarios.query.filter_by(cpf = cpf ).first():
            return{"error":"CPF já cadastrado"}
        if Usuarios.query.filter_by(email = email ).first():
            return{"error":"E-mail já cadastrado"}

        usuario = Usuarios(nome = nome, email = email, senha = senha , cpf = cpf, nascimento = nascimento, 
                            carrinho_id = carrinho_id, telefone = telefone, telefone_opicional = telefone_opicional)

        db.session.add(usuario)
        db.session.commit()

        return usuario.json() , 200

@usuario_api.route('/usuarios/<int:id>',methods = ['GET','PUT','PATCH','DELETE'])
def pagina_usuario(id):

    usuario = Usuarios.query.get_or_404(id)

    if request.method == "GET":
        return usuario.json(),200
    
    if request.method =='PUT':
        dados = request.json        
        nome = dados.get('nome')
        email = dados.get('email')
        senha = dados.get('senha')
        cpf = dados.get('cpf')
        nascimento = dados.get('nascimento')
        carrinho_id = dados.get('carrinho_id')
        telefone = dados.get('telefone')
        telefone_opicional = dados.get('telefone_opicional')

        error = testar_entradas(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional)
        if (error != False):
            return error

        if (usuario.cpf != cpf) and (Usuarios.query.filter_by(cpf = cpf ).first()):
            return{"error":"CPF já cadastrado"}
        if (usuario.email != email) and (Usuarios.query.filter_by(email = email ).first()):
            return{"error":"E-mail já cadastrado"}
        
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        usuario.cpf = cpf
        usuario.nascimento = nascimento
        usuario.telefone = telefone
        usuario.telefone_opicional = telefone_opicional
        usuario.carrinho_id = carrinho_id

        db.session.commit()
        return usuario.json() , 200

    if request.method == "PATCH":
        dados = request.json        
        nome = dados.get('nome', usuario.nome)
        email = dados.get('email', usuario.email)
        senha = dados.get('senha', usuario.senha)
        cpf = dados.get('cpf', usuario.cpf)
        nascimento = dados.get('nascimento', usuario.nascimento)
        telefone = dados.get('telefone', usuario.telefone)
        telefone_opicional = dados.get('telefone_opicional', usuario.telefone_opicional)
        carrinho_id = dados.get('carrinho_id',usuario.carrinho_id)
        
        error = testar_entradas(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional)
        if (error != False):
            return error
        
        if (usuario.cpf != cpf) and (Usuarios.query.filter_by(cpf = cpf ).first()):
            return{"error":"CPF já cadastrado"}
        if (usuario.email != email) and (Usuarios.query.filter_by(email = email ).first()):
            return{"error":"E-mail já cadastrado"}
        
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        usuario.cpf = cpf
        usuario.nascimento = nascimento
        usuario.telefone = telefone
        usuario.telefone_opicional = telefone_opicional
        usuario.carrinho_id = carrinho_id 

        db.session.commit()
        return usuario.json() , 200
    
    if request.method =='DELETE':
        db.session.delete(usuario)
        db.session.commit()
        return usuario.json(), 200