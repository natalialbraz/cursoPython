"""
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    print('Caractere inválido! Tente outra vez.')
    sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso' .format(sexo))


import random
computador = random.randint(0,10)
j = int(input('Tente adivinhar o numero que o computador pensou: '))
c = 0
print(computador)
while j != computador:
    c += 1
    print('Errou!')
    j = int(input('Tente adivinhar o numero que o computador pensou: '))
print('Parabens! Você acertou depois de {} tentativas.' .format(c+1))


n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))
op = 0
while op != 5:
    print('''[1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        soma = n1+n2
        print('A soma dos numeros é {}' .format(soma))
    elif op == 2:
        mult = n1*n2
        print('A multiplicação dos numeros é {}' .format(mult))
    elif op == 4:
        a = int(input('Digite um novo numero: '))
        b = int(input('Digite outro novo numero: '))
    elif op == 3:
        if n1>n2:
            maior = n1
        else:
            maior = n2
        print('O maior numero é {}' .format(maior))
    elif op == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida. tente novamente')

print('Fim do programa!')


from math import factorial
n = int(input('Digite um numero: '))
f = factorial(n)
print('O fatorial de {} é {}' .format(n, f))


n = int(input('Digite um numero: '))
c = n
fat = 1
print('Calculando {}! = ' .format(n))
while c > 0:
    fat = fat*c
    c = c-1
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
print('{}' .format(fat))


t1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razao da PA: '))
print('A progressão geométrica é:\n{}' .format(t1))
p = t1
c = 0
while c < 9:
    p = p+r
    print('{}' .format(p))
    c = c+1



t1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razao da PA: '))
print('A progressão geométrica é: ')

p = t1
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{}'.format(p))
        p = p+r
        c = c+1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print('FIM DO PROGRAMA')


#sequencia de fibonacci
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {} ' .format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' -> {}' .format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1



n = int(input('Digite um número inteiro: '))
s = 0
c = 0
while n != 999:
    s = s+n
    c = c + 1
    n = int(input('Digite um numero inteiro: '))

print('Foram digitados {} números. A soma deles é {}' .format(c, s))

"""

op = 's'
soma = 0
cont = 0
maior = 0
menor = 100000000
while op == 's':
    n = int(input('Digite um número: '))
    soma = soma + n
    cont = cont + 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    op = str(input('Você deseja continuar digitando valores? '))

media = soma/cont
print('A media dos valores lidos é {}' .format(media))
print('O maior valor lido é {}' .format(maior))
print('O menor valor lido é {}' .format(menor))


    





