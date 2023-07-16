#Variavel

#Números
velocidade_internet = 10
print(velocidade_internet)

#float
nota_filme = 8.5

#Valores Boleanos
esta_aberto = True

#Strings
nome_do_curso = 'Lógica de Programação'

#como as variaveis seriam utilizadas em um programa?
#Problema 1 valor por hora
#Escreva um programa que retorna o valor hora de um funcionario com base no seu sálario mensal e horas trabalhadas por mes.

salario_mensal = input ('Qual é o seu salario mensal?')
horas_trabalhadas = input ('Quantas horas trabalhadas por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas) #int é para transformar o valor inserido em valor inteiro
print(valor_hora)