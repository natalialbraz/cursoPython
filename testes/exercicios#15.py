"""
s = 0
c = 0
while True:
    n = int(input('Digite numeros: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} números. A soma entre eles é {s}')


c = 0
while True:
    n = int(input('Informe o número que deseja saber a tabuada: '))
    c = 0
    if n < 0:
        print('FINALIZANDO...')
        break
    while c <= 10:
        mult = c*n
        print(f'Tabuada de {n}:\n{n}x{c} = {mult}')
        c += 1



import random
v = 0
while True:
    computador = random.randint(0, 10)
    j1 = int(input('Digite um valor: '))
    total = j1 + computador
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
        print(f'COMPUTADOR: {computador}\n JOGADOR: {j1} ')
        print(f'O total da jogada foi {total}')
    if op == 'P':
        if total % 2 == 0:
            v += 1
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    elif op == 'I':
        if total % 2 != 0:
            v += 1
            print('Você venceu!')
        else:
            print('Você perdeu! ')
            break
print(f'Você teve {v} vitórias consecutivas.')


contm = 0
conth = 0
c = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual seu sexo? [F/M] ')).strip().upper()[0]
    if idade >= 18:
        contm += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        c += 1

    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Foram cadastradas {contm} pessoas com mais de 18 anos')
print(f'Foram cadastrados {conth} homens')
print(f'{c} mulheres cadastradas têm menos de 20 anos.')


ptotal = 0
contmm = 0
barato = 0
bprod = ''
print('LOJA BEM VIVER')
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    ptotal += preço
    if preço > 1000:
        contmm += 1
    if preço < barato:
        barato = preço
        prodb = produto
    op = str(input('Deseja continuar cadastrando produtos? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'O total gasto na compra foi R${ptotal:.2f}')
print(f'{contmm} produtos custam mais de R$1000,00')
print(f'{prodb} é o produto mais barato')

"""

print('Caixa Eletrônico Santader')
valor = int(input('Qual valor você deseja sacar? '))
print('Cédulas disponíveis: R$1,00 / R$10,00 / R$20,00 / R$50,00 ')
total = valor
ced = 50
totalc = 0
while True:
    if total >= ced:
        total -= ced
        totalc += 1
    else:
        if totalc > 0:
            print(f'Total de {totalc} cédulas de R${ced}')
        if ced == 50:
            ced = 20
            totalc = 0
        elif ced == 20:
            ced = 10
            totalc = 0
        elif ced == 10:
            ced = 1
            totalc = 0
        if total == 0:
            break

