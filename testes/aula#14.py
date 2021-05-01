#estrutura de repetição while
"""
c  = 1
while c<10:
    print(c)
    c = c + 1     # = c += 1


r = 's'
while r == 's':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? s/n'))

"""
n = 1
contp = 0
conti = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        contp += 1
    else:
        conti += 1
print('O total de numeros pares digitados é {}' .format(contp))
print('O total de numeros impares digitados é {}' .format(conti))
