""""
Portfólio de Algoritmos e Programação de Computadores
Daniel Alves de Sousa

"""
'''
3º Ponto Flutuante ou Decimal (float)

"O ponto flutuante é um tipo de dado composto
por caracteres numéricos (dígitos) decimais e 
é amplamente conhecido como um tipo usado para 
representar números racionais, que podem ser 
informalmente chamados de 'números fracionados'."

'''

#Exemplo de como ele pode ser utilizado:


#A função calcular_impostos é definida com 
# um único argumento produtos, que é uma lista 
# de dicionários representando produtos.

def calcular_impostos(produtos):
    
    #Dentro da função, uma variável total_impostos
    # é inicializada com o valor 0.0. Esta variável 
    # será usada para acumular o valor total dos impostos 
    # a serem pagos.
    
    total_impostos = 0.0
    
    #Em seguida, o código entra em um loop for que itera 
    # sobre cada produto na lista produtos.
    
    for produto in produtos:
        
        #Para cada produto, as informações relevantes são extraídas 
        # do dicionário. preco_unitario é o preço unitário do produto 
        # e taxa_de_imposto é a taxa de imposto  aplicada a esse produto.
        
        preco_unitario = produto["preço_unitário"]
        taxa_de_imposto = produto["taxa_de_imposto"]
        
        #O imposto para o produto atual é calculado multiplicando preco_unitario 
        # por taxa_de_imposto e o resultado é armazenado na variável imposto.
        
        imposto = preco_unitario * taxa_de_imposto
        
        #O imposto para o produto atual é calculado multiplicando preco_unitario por
        # taxa_de_imposto e o resultado é armazenado na variável imposto.
        
        total_impostos += imposto
        
    #O imposto calculado para o produto atual é então adicionado ao total_impostos para 
    # acumular o valor total dos impostos a serem pagos.
    
    return total_impostos

#O loop continua até que todos os produtos na lista produtos tenham sido processados.
#Finalmente, a função retorna o valor total de impostos calculado.

produtos = [
    
    #Fora da função, uma lista produtos é definida com três produtos, cada um representado 
    # como um dicionário com um nome, preço unitário e taxa de imposto.
    
    {"nome": "Produto 1", "preço_unitário": 19.99, "taxa_de_imposto": 0.08},
    {"nome": "Produto 2", "preço_unitário": 29.99, "taxa_de_imposto": 0.05},
    {"nome": "Produto 3", "preço_unitário": 9.99, "taxa_de_imposto": 0.10}
]

#A função calcular_impostos é chamada com a lista de produtos como argumento, e o valor retornado 
# é armazenado na variável total_impostos.

total_impostos = calcular_impostos(produtos)

#O resultado é então impresso usando uma f-string formatada com quatro casas decimais de precisão 
# para exibir o valor total de impostos com clareza.

print(f"O valor total de impostos a serem pagos é: {total_impostos:.4f}")


'''
Código completo:

def calcular_impostos(produtos):
    total_impostos = 0.0

    for produto in produtos:
        preco_unitario = produto["preço_unitário"]
        taxa_de_imposto = produto["taxa_de_imposto"]
        imposto = preco_unitario * taxa_de_imposto
        total_impostos += imposto

    return total_impostos

produtos = [
    {"nome": "Produto 1", "preço_unitário": 19.99, "taxa_de_imposto": 0.08},
    {"nome": "Produto 2", "preço_unitário": 29.99, "taxa_de_imposto": 0.05},
    {"nome": "Produto 3", "preço_unitário": 9.99, "taxa_de_imposto": 0.10}
]

total_impostos = calcular_impostos(produtos)
print(f"O valor total de impostos a serem pagos é: {total_impostos:.4f}")


'''