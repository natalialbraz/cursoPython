"""
dados = {}
dados['Nome'] = str(input('Qual é o nome? '))
dados['Média'] = int(input('Qual é a media do aluno? '))

if dados['Média'] >= 6:
    dados['Situação']  = 'Aprovado'
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'

else:
    dados['Situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}')





import random
from time import sleep
from operator import itemgetter
jogo = {'jogador1': random.randint(1, 6),
        'jogador2': random.randint(1, 6),
        'jogador3': random.randint(1, 6),
        'jogador4': random.randint(1, 6)}
print('Valores sorteados: ')
ordem = dict()
print(f'RANKING DOS JOGADORES')
for k, v in jogo.items():
        print(f'{k} tirou {v} no dado.')
        sleep(2)
ordem = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ordem):
        print(f'{i+1}º lugar:  {v[0]} com {v[1]} pontos')


from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Digite o seu nome completo: '))
ano = int(input('Digite seu ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - ano
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Em qual ano foi contratado? '))
    cadastro['Salário'] = float(input('Informe seu salário: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - datetime.now().year)
for k, v in cadastro.items():
    print(f'{k} = {v}')



registro = dict()
partidas = list()
registro['Nome'] = str(input('Nome do jogador: '))
qtde = int(input(f'Número de partidas jogadas pelo {registro["Nome"]}: '))
for c in range(0, qtde):
    partidas.append(int(input(f'Quantidade de gols feitos na partida {c+1}:')))
registro['Gols'] = partidas[:]
registro['Total'] = sum(partidas)
for k, v in registro.items():
    print(f'{k} = {v}')
print(f'O jogador {registro["Nome"]} jogou {len(registro["Gols"])} partidas.')




pessoas = dict()
lista = list()
mulheres = list()
somai = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Digite o nome: '))
    pessoas['Sexo'] = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    while pessoas['Sexo'] not in 'MF':
        print(f'Você digitou o sexo errado. Digite novamente.')
        pessoas['Sexo'] = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    pessoas['Idade'] = int(input('Digite a idade: '))
    somai += pessoas['Idade']
    lista.append(pessoas.copy())
    op = str(input('Deseja registrar mais pessoas? [S/N] ')).strip().upper()[0]
    if op != 'S':
        break

media = somai/(len(lista))
print(lista)
print(f'Quantidade de pessoas cadastradas = {len(lista)}')
print(f'A media de idade é {media} anos.')
print(f'Mulheres cadastradas: ', end='')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print(f'As pessoas que estão com a idade acima da média são: ',end='')
for i in lista:
    if i['Idade'] >= media:
        print(f'{i["Nome"]} ', end='')

"""

registro = dict()
partidas = list()
time = list()
while True:
    registro.clear()
    partidas.clear()
    registro['Nome'] = str(input('Nome do jogador: '))
    qtde = int(input(f'Número de partidas jogadas pelo {registro["Nome"]}: '))
    for c in range(0, qtde):
        partidas.append(int(input(f'Quantidade de gols feitos na partida {c+1}:')))
    registro['Gols'] = partidas.copy()
    registro['Total'] = sum(partidas)
    time.append(registro.copy())
    op = str(input('Deseja cadstrar novos jogadores? [S/N] ')).strip().upper()[0]
    if op != 'S':
        break
print('-='*30)
print('cod ', end='')
for i in registro.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar os dados de qual jogador? '))
    if busca == 999:
        print('ENCERRANDO CONSULTA...')
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-'*40)



"""
for k, v in registro.items():
    print(f'{k} = {v}')
print(f'O jogador {registro["Nome"]} jogou {len(registro["Gols"])} partidas.')

"""




