#Medidor de Velocidade
'''
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua, crie um programa que recebe do usuário
um valor que representa a velocidade e com base nessa velocidade, diga se ela tomou uma multa leve, grave ou gravissima.
Levando em consideração que se a pessoa estiver abaixo da velocidade maxima, o programa deve exibir" não houve multa, caso
esteja até 10km acima, deve exibir "levou multa leve", caso esteja entre 11 a 20km acima, deve exibir "levou multa grave"
e se estiver acima de 20km do permitido, exiba "levou multa gravissima

Analise criticamente o problema e descubra:
(tente explicar em voz alta para si mesmo, peça mais info e procure na net para resolver)

1. Quais são os dados de entrada necessários?
o valor maximo permitido
valor das penalidades
valor do Usuario
2. O que devo fazer com estes dados?
armazenar o valor maximo permitido
bater o valor inserido do usuario com o banco de dados sobre o valor maximo e as penalidades
3. Quais são as restirções deste problema?
o valor tem que ser um numero positivo
valor inteiro
valor acima de 0
4. Qual é o resultado esperado?
o sistema volte ao usuario o tipo de punição que ele recebeu ou se não recebeu punição
5. Qual é a sequencia de passos a ser feitas para chegar ao resultado esperado?
ValorPermitido = 80
ValorPunicao1 = (81,90)
ValorPunicao2 = (91,100)
ValorPunicao3 = (101 para cima)
input ValorUsuario
if ValorUsuario <= ValorPermitido = sem punição
if ValorUsuario = ValorPunicao1 = multa leve
if ValorUsuario = ValorPunicao2 = Multa grave
if ValorUsuario = ValorPunicao3 = Multa gravissima
'''

velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('não levou multa')
elif velocidade >= velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('multa grave')
elif velocidade >= velocidade_maxima + 20:
    print('multa gravissima')