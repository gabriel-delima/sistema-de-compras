from app.extensions import CPF
import re


# Função usada para validar as entradas de cada campo do usuário. 
#     obs.: sem considerar as validações para cpf/email único
def testar_entradas_usuario(nome,email,senha,cpf,nascimento,carrinho_id,telefone,telefone_opicional):

    # Validar Campos Obrigatórios
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

    # Validar tipo dos campos
    if (not(isinstance(nome,str)) or 
        not(isinstance(email,str)) or 
        not(isinstance(senha,str)) or
        not(isinstance(cpf,int)) or 
        not(isinstance(nascimento,str)) or
        not(isinstance(telefone,int)) or 
        (telefone_opicional != None and not(isinstance(telefone_opicional,int)))):
        
        return{"error":"Algum tipo inválido"},400
    
    # Validar inteiros negativos
    if (telefone_opicional != None and telefone_opicional<0) or (telefone<0) or (cep<0):
        return{"error":"Os telefones e o Cep devem ser inteiros positivos"},400

    # Validar tamanho dos campos
    if len(nome) > 50:
        return{"error":"Nome deve conter até 50 caracteres"},400
    if len(email) > 50:
        return{"error":"E-mail deve conter até 50 caracteres"},400
    if len(senha) > 30:
        return{"error":"Senha deve conter até 30 caracteres"},400
    if len(str(cpf)) != 11:
        return{"error":"CPF deve conter 11 dígitos"},400
    if (len(nascimento) != 10):
        return{"error":"Nascimento deve estar no formato xx/xx/xxxx (x -> inteiros positivos)"},400

    #Validar carrinho_id
    if (carrinho_id != None) and (not(isinstance(carrinho_id,int)) or (carrinho_id<0)) :
        return{"error": "carrinho_id deve ser inteiro positivo"}

    #Validar formato da data
    if ((nascimento[2] != "/") or (nascimento[5] != "/") or 
        not(nascimento[0].isdigit()) or not(nascimento[1].isdigit()) or
        not(nascimento[3].isdigit()) or not(nascimento[4].isdigit()) or 
        not(nascimento[6].isdigit()) or not(nascimento[7].isdigit()) or not(nascimento[8].isdigit()) or not(nascimento[9].isdigit())):
        
        return{"error":"Nascimento deve estar no formato xx/xx/xxxx (x -> inteiros positivos)"},400

    #Validar cpf
    if not(CPF().validate(str(cpf))):
        return{"error":"CPF Inválido"},400
        
    #validar email usando RegEx (não garante e-mail 100% válido mas verifica a grande maioria dos erros)
    # a verificação leva em consideração: 
    #   1 - e-mail no formato xxxxxxxx@xxxxxxxx.xxxxxxxx
    #   2 - parcela antes do "@" deve conter apenas letras, números, "." e "_"
    #   3 - e-mail não pode começar com "." ou "_" e deve conter no mínimo 2 caracteres antes do "@"
    #   4 - parcela depois do "@" e antes do "." deve conter apenas letras ou números
    #   5 - parcela depois do "." deve conter apenas letras ou "." e ter no máximo 50 caracteres
    validar_email = re.search("^[a-zA-Z0-9]+[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z.]{1,50}$",email)
    if (validar_email == None):
        return{"error":"Email Inválido"},400

    return False