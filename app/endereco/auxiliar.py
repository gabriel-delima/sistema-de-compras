
# Função usada para validar as entradas de cada campo do endereco. 
def testar_entradas_endereco(cep,logadouro,numero,complemento,bairro,cidade,estado,usuario_id):
    
    # Validar Campos Obrigatórios
    if cep is None:
        return{"error":"Cep Obrigatório"},400
    if logadouro is None:
        return{"error":"Logadouro Obrigatório"},400
    if numero is None:
        return{"error":"Numero Obrigatório"},400
    if bairro is None:
        return{"error":"Bairro Obrigatório"},400
    if cidade is None:
        return{"error":"Cidade Obrigatório"},400
    if estado is None:
        return{"error":"Estado principal Obrigatório"},400

    # Validar tipo dos campos
    if (not(isinstance(cep,int)) or 
        not(isinstance(logadouro,str)) or 
        not(isinstance(numero,int)) or 
        not(isinstance(bairro,str)) or
        not(isinstance(cidade,str)) or 
        not(isinstance(estado,str)) or
        (complemento != None and not(isinstance(complemento,str)))):
        
        return{"error":"Algum tipo inválido"},400

    # Validar inteiros negativos 
    if (numero < 0) or (cep < 0):
        return{"error":"Cep e Numero devem ser inteiros positivos"},400
        
    # Validar tamanho dos campos
    if len(str(cep)) != 8:
        return{"error":"Cep deve conter 8 dígitos"},400
    if len(logadouro) > 50:
        return{"error":"Logadouro deve conter até 50 caracteres"},400
    if len(bairro) > 50:
        return{"error":"Bairro deve conter té 50 caracteres"},400
    if len(cidade) > 50:
        return{"error":"Cidade deve conter até 50 caracteress"},400
    if (len(estado) > 50):
        return{"error":"Estado deve conter até 50 caracteres"},400

    #Validar usuario_id
    if (usuario_id != None) and (not(isinstance(usuario_id,int)) or (usuario_id<0)) :
        return{"error": "usuario_id deve ser inteiro positivo"}

    return False