#listas pt 2
"""
dados = list()
dados.append('Pedro')
dados.append(25)
pessoas = list()
#faz uma copia da lista DADOS,colocando-a dentro da lista
#pessoas/ assim o indice 0 de pessoas estará ocupado com as
#informações da lista DADOS

pessoas.append(dados[:])


#tambem é possivel declarar isso tudo de uma vez só
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])


teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
#galera.append(teste)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
#galera.append(teste)
galera.append(teste[:])
print(galera)
#dessa maneira esperava-se que mostrasse a lista TESTE com
#os dados do Gustavo e GALERA com os dados da Maria
#mas quando fazemos galera.append(teste) as duas listas
#passam a ter uma ligação, de forma que alteações em uma
#tambem alteram a outra
#para que isso não aconteça devemos criar uma
# copia: galera.append(teste[:])


#formas de declarar uma lista dentro de outra
galera = [['João', 19], ['Ana', 33], ['Joaquim', 45], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

"""
#entrando com dados em lista dentro de outr
galera = list()
dado = list()
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
    else:
        print(f'{p[0]} é menor de idade.')


