# Função usada para validar as entradas de cada campo do produto_compra. 
def testar_entradas_produto_compra(quantidade,valor_unitario,produto_id):
    # Validar Campos Obrigatórios
    if quantidade is None:
        return{"error":" Quantidade Obrigatória"},400
    if valor_unitario is None:
        return{"error":" Valor unitário Obrigatório"},400
        
    # Validar tipo dos campos
    if ( not(isinstance(quantidade,int)) or 
         not(isinstance(valor_unitario,int))):

        return{"error":"Algum tipo inválido"},400
        
    # Validar inteiros negativos 
    if (quantidade < 0) or (valor_unitario < 0) :
        return{"error":"Os valores devem ser inteiros positivos"},400
        
    #Validar produto_id
    if (produto_id != None) and (not(isinstance(produto_id,int)) or (produto_id<0)) :
        return{"error": "produto_id deve ser inteiro positivo"}

    return False