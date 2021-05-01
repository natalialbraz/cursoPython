"""
lista = list()
dados = list()
maior = 0
menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
            nmaior = dados[0]
        if dados[1] < menor:
            menor = dados[1]
            nmenor = dados[0]
    lista.append(dados[:])
    dados.clear()

    op = str(input('Deseja cadastrar mais pessoas? [S/N]')).strip().upper()[0]
    if op != 'S':
        break

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi {maior} da {nmaior}')
print(f'O menor peso foi {menor} da {nmenor}')


unica = [[], []]
valor = 0
for c in range (0,7):
    valor = (int(input('Digite um numero: ')))
    if valor % 2 == 0:
        unica[0].append(valor)
    else:
        unica[1].append(valor)
unica[0].sort()
unica[1].sort()

print(f'Lista dos numeros par em ordem crescente = {unica[0]}')
print(f'Lista dos números ímpares em ordem crescente = {unica[1]}')


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um valor: '))


for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


spar = 0
soma3 = 0
maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um numero: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print(f'A soma de todos os valores pares é {spar}')
for l in range(0, 3):
    soma3 += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {soma3}')
for c in range(0, 3):
    if matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')



import random
lista = list()
jogos = list()

q = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0
while tot <q:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'SORTEANDO {q} JOGOS')
for i, l in enumerate(jogos):
    print(f'Jogo {i}: {l}')

"""
aluno = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1+n2)/2
    aluno.append([nome, [n1, n2], media])
    op = str(input('Deseja cadastrar mais alunos? [S/N] ')).strip().upper()[0]
    if op != 'S':
        break
print(f'{"Num.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        break
    if opc <= len(aluno)-1:
        print(f'Notas de {aluno[opc][0]} são {aluno[opc][1]}')















