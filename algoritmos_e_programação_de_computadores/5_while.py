""""
Portfólio de Algoritmos e Programação de Computadores
Daniel Alves de Sousa

"""
"""
5º While

É uma estrutura de repetição utilizada quando queremos que 
determinado bloco de código seja executado ENQUANTO (While)
determinada função for satisfeita.

"""
numero = int(input("Digite um número (digite 0 para sair): "))

while numero != 0:
    if numero > 0:
        print("O número é positivo.")
    else:
        print("O número é negativo.")
    numero = int(input("Digite um número (digite 0 para sair): "))

print("Você saiu do programa.")

#1- O programa começa pedindo ao usuário que insira um número inteiro usando input(),
# que é então convertido em um número inteiro com int() e armazenado na variável numero.

#2- Em seguida, ele entra em um loop while. Enquanto numero for diferente de 0, o código 
# dentro do loop será executado. Isso significa que o loop continuará a ser executado até 
# que o usuário digite 0 para sair.

#3- Dentro do loop, há uma verificação condicional if que verifica se o número é maior que 0 ou não. 
# Dependendo do resultado da verificação, ele imprime se o número é positivo ou negativo.

#4- Após a impressão, o programa solicita novamente ao usuário que insira um número.

#5- Se o usuário inserir 0, o while loop não será mais executado, e o programa imprimirá 
# "Você saiu do programa."
