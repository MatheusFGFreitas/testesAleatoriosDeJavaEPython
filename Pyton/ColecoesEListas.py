#Coleções(listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200

#agora é a lista, onde é mais facil
precos = [20,50,200]
#Indices  0  1  2
print(precos[1])
print(precos[0])
print(precos.index(200)) #descobrir o indices para ver o local do valor 200
# Lista
diversidades = [15,'Matheus',True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
# Laços em iteráveis
for preco in precos:
    print(preco)

#exemplo
'''
some os valores
dados uma coleçao de daos "idades"[15,46,75,34,23], imprima na tela a soma desses valores

Pseudocodigo
idades = [15,46,75,34,23]
total = 0
loop idade em idades
total = total + idade
print total
'''

idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
print(total)