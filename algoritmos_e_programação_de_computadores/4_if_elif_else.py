""""
Portfólio de Algoritmos e Programação de Computadores
Daniel Alves de Sousa

"""
"""
3º if - elif - else (se - senão se - senão )

As construções if, elif e else em Python são usadas 
para criar ramificações condicionais em seu código, 
permitindo que você execute diferentes blocos de código
com base em condições específicas. Eles desempenham um papel
fundamental na tomada de decisões em programas Python.

"""
#Exemplo de como pode ser aplicado if - elif - else:

idade = int(input("Digite a sua idade: "))
if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

#1- Inicia o programa com o usuário digitando a sua idade.

#2- If é utilizado para saber se a idade do usuário é menor que 18 anos.
# (menor de idade)

#3- Elif é utilizado para testar outra condição caso if seja falsa.
# se for maior ou igual a 18, ao mesmo tempo, vai verificar se é 
# menor que 65 anos. (adulto)

#4- Else se nenhuma das condições anteriores forem verdadeira. (idoso)