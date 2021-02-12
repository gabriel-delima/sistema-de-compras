# Função usada para validar as entradas de cada campo do carrinho. 
def testar_entradas_carrinho(valor_frete,valor_total,usuario_id):
    
    # Validar tipo dos campos
    if ( not(isinstance(valor_frete,int)) or 
         not(isinstance(valor_total,int)) ):

        return{"error":"Algum tipo inválido"},400
        
    # Validar inteiros negativos 
    if (valor_frete < 0) or (valor_total < 0):
        return{"error":"Os valores devem ser inteiros positivos"},400
        
    #Validar usuario_id
    if (usuario_id != None) and (not(isinstance(usuario_id,int)) or (usuario_id<0)) :
        return{"error": "usuario_id deve ser inteiro positivo"}

    return False