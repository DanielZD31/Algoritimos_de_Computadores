""""
Portfólio de Algoritmos e Programação de Computadores
Daniel Alves de Sousa

"""
"""
2º Algoritmos para realizar operações de:

1- Adição
2-Subtração
3-Multiplicação
4-Divisão
5-Porcentagem 
"""
#Adição
print("Adição: ")
# Solicita dois números ao usuário e realiza a adição
#num : é a variável
#floaat(): é usado para converter o valor digitado pelo usuário em um número real.
#print(): imprima o texto ou valor na tela
# + : operador da soma de dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)
print('=' * 30)

#Subtração
print("Subtração: ")
# Solicita dois números ao usuário e realiza a subtração
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
subtracao = num1 - num2
print("A subtração é:", subtracao)
print('=' * 30)

#Multiplicação
print("Multiplicação: ")
# Solicita dois números ao usuário e realiza a multiplicação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
multiplicacao = num1 * num2
print("A multiplicação é:", multiplicacao)
print('=' * 30)

#Divisão
print("Divisão: ")
# Solicita dois números ao usuário e realiza a divisão
#O comando if-else: Permite executar alguns comandos se uma 
#condição for verdadeira (if) e outros se ela for falsa (else).
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num2 != 0:
    divisao = num1 / num2
    print("A divisão é:", divisao)
else:
    print("Erro: Divisão por zero não é permitida.")
    
print('=' * 30)

#Porcentagem
print("Porcentagem: ")
# Calcula a porcentagem de um número em relação a outro
valor_total = float(input("Digite o valor total: "))
percentual = float(input("Digite o percentual a ser calculado: "))

resultado = (percentual / 100) * valor_total
print(f"{percentual}% de {valor_total} é igual a {resultado}")
print('=' * 30)


