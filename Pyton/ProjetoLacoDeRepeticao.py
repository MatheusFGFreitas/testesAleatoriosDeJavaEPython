# Projeto - Chute o número
'''
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um numero até que o
valor gerado aleatóriamente seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no inicio do programa.

# Método 5Q's para montar um algoritimo:

Analise criticamente o problema e descubra:
(tente entender o problema, explique para si mesmo e peça informações, ou pesquise até comprrender)

1. Quais são os dados de entrada necessários?
valor aleatorio gerado automaticamente
valor inserido pelo usuario
2. O que devo fazer com estes dados?
o valor aleatorio deve ser armazenado e deve comparar o chute do usuario pelo valor armazenado, com isso dizer se o valor
foi maior, menor ou igual ao valor
3. Quais são as restrições deste problema?
a restrição é o valor inteiro, e entre os numeros de 1 a 10
4. Qual é o resultado esperado?
caso o numero inserido pelo usuario seja maior que o numero aleatorio, ele tenta novamente, caso menor ele tenta novamente
e se for o mesmo numero, o programa anuncia que acertou e encerra o programa
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
usuario input valor de 1 a 10
if ValorUsuario foi maior que o numero aleatorio feito
    print(numero maior, tente novamente)
if ValorUsuario for menor que o numero aleatorio feito
    print(numero menor, tente novamente)
else ValorUsuario for o mesmo numero aleatorio feito
    print(você acertou, parabens!)
encerra o programa
'''

import random #bibiloteca do proprio pyton para fazer um valor aleatorio

ValorAleatorio = random.randint(1,10)
acertou = False #isso identifica que é para manter o programa rodando até acertar
while acertou == False: #aqui ira fazer o programa continuar rodando os determinados processos até acertar
    chute = int(input('Chute um valor inteiro de 1 a 10: ')) #colocado abaixo para não ficar preso no laço de repetição
    if chute > ValorAleatorio:
        print('Chute foi maior que o valor gerado, tente novamente')
    elif chute < ValorAleatorio:
        print('Chute foi menor que o valor gerado, tente novamente')
    elif chute == ValorAleatorio:
        acertou = True
        print('Parabéns você acertou')