#Fatorial de um número
'''
Crie um programa que recebe um número e imprime o seu fatorial.
#método 5Q's para montar um algoritimo:
Analise criticamente o problema e descubra:
(dica: explique o problema em voz alta para você mesmo, e caso não entenda, descubra no google ou chat gpt por exemplo)

1. Quais são os dados de entrada necessários?
um numero
2. O que devo fazer com esses dados?
eu devo calcular o fatorial do número que for passado para o meu programa e o exibir na tela.
3. Quais são as restrições desse problema?
o número deve ser um valor positivo e deve ser um valor inteiro
4. Qual é o resultado esperado?
o resultado esperado é que o fatorial do número providenciado seja mostrado
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
input de um numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print(fatorial)
'''
numero = int(input('Digite um número positivo e inteiro'))
if numero > 0:
    fatorial = 1
    for item in range (1,numero +1):
        fatorial = fatorial * item
    print(fatorial)