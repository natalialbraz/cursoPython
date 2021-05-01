"""
lista = [int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite outro: ')),
         int(input('Digite o ultimo valor: '))]
maior = 0
menor = 10000000000000000
for c in range(0, len(lista)):
    if lista[c] < menor:
        menor = lista[c]
    if lista[c] > maior:
        maior = lista[c]
print(f'O maior digitado foi {maior}.' ,end='')
print(f'Ele estava na posição {lista.index(maior)}')
print(f'O menor valor digitado foi {menor}.' ,end='')
print(f'Ele estava na posição {lista.index(menor)}')


lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado! ')


    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op in 'N':
        break
lista.sort()
print(f'Os valores digitados em ordem crescente são: {lista}')


l = list()
for c in range(0,5):
    v = int(input('Digite um número: '))
    if c == 0 or v > l[len(l)-1]:
        l.append(v)
    else:
        pos = 0
        while pos < len(l):
            if v <= l[pos]:
                l.insert(pos, v)
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {l}')




lista = []
while True:
    v = int(input('Digite um número: '))
    lista.append(v)
    op = str(input('Deseja digitar mais valores? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Foram digitadods {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {lista}')
if 5 in lista:
    print(f'O valor 5 foi digitado.')
else:
    print(f'O valor 5 não foi digitado.')




lista = []
lpar = []
limpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lpar.append(n)
    else:
        limpar.append(n)
    op = str(input('Deseja digitar mais números? [S/N] ')).strip().upper()[0]
    if op != 'S':
        break

print(f'Lista inicial = {lista}')
print(f'Lista extra par = {lpar}')
print(f'Lista extra impar = {limpar}')

"""

exp = str(input('Digite a expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida! ')
else:
    print('Sua expressão está errada!')





