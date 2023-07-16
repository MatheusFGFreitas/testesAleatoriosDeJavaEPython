#Laços de Repetição + Listas
print('carregando')
print('carregando')
print('Carregando')

#agora o laço de repetição ira diminuir a quantidade de codigos

for palavra in range(1,6):
    print('carregando')

for item in range(1,21): #esse codigo irá printar a numeração que contem dento dos parenteses, porém o 21 é que ele para em um numero antes, logo é do 1 ao 20
    print(item)

for item in range(1,20,2): #esse codigo ira pular o numero de 2 em 2
    print(item)

#lista em pyton
nomes = ['Matheus','Ester','Gabriel','Otávio']#graças a esse comando, e essa separação em , a lista nomes foi criada com todos os nomes
for nome in nomes: #pode ser qualquer coisa, nomes, aniversarios, etc...
    print(nome)

'''
problema 1:
imprima os valores de 1 a N
'''

valor_maximo = int(input('digite o valor máximo')) #o int pode ser inserido na 1 parte, porém adicionando mais uma chave de parenteses
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo + 1): #o +1 é para chegar ao valor maximo inserido, ja que o valor sempre será 1 menor
    print(numero)