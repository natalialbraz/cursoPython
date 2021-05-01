a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('terceiro valor:'))
if a>b and a>c:
    print('o maior numero e {}' .format(a)) #identacao e usada para formar o bloco de comando
elif b>a and b>c:
    print('o maior numero e {}' .format(b))
else:
    print('o maior numero e {}' .format(c))
print('final do programa') #nao esta dentro da estrutura condicional, entao sera impresso de qualquer jeito