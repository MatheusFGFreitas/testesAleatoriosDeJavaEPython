#condicionais

#as condicionais mais usadas são if, elif e else

'''
Problema: 
E ae Matheus, bora jogar?
Se eu terminar o trampo, dá pra dale
'''
trabalho_terminado = True #se for true escrito aqui, saira bola dale, se for false, Dá não menor
if trabalho_terminado == True:
    print('Bora dale')
else:
    print('Dá não menor')

'''
Problema 2:
Ei, me ajuda aqui com a mudança?
Se eu tiver livre ajudo sim, caso não peça para o meu irmão
'''

estou_livre = False
if estou_livre == True:
    print('Ok te ajudo')
else:
    print('Dá não, pede pro meu irmão')

'''
Problema 3:
eu cheguei atrasado na aula, posso entrar?
se não atrasou pela 3 vez, então sim, caso contrario, levara suspensão
'''

numero_de_atrasos = input('chegou atrasado, se tiver 3 atrasos você esta suspenso, você se atrasou quantas vezes?') #input é para o usuario responder a pergunta
if int(numero_de_atrasos) >= 3:
    print('Você está suspenso')
elif int(numero_de_atrasos) == 2:
    print('pode entrar, porém na proxima você está suspenso')
elif int(numero_de_atrasos) == 1:
    print('pode entrar, mas cuidado, mais duas faltas você vai ser suspenso')
else:
    print('Pode entrar')

#variavel para descobrir valor maior pelos valores inclusos pelo usuario

primeiro_valor = input('Digite o 1 valor')
segundo_valor = input('Digite o 2 valor')

if int(primeiro_valor) > int(segundo_valor):
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')
