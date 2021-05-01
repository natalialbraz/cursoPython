"""
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1+n2
print('A soma entre {} e {} vale {}' .format(n1, n2, s))

l1 = (input('Informe um numero:'))
print(type(l1))
print(l1.isalpha())
"""
a = input('Digite algo:')
print('O tipo primitivo desse valor e {} ' .format(type(a)))
print('So tem espaços? {}' .format(a.isspace()))
print('É um número? {}' .format(a.isnumeric()))
print('É alfabético? {}'.format(a.isalpha()))
print('É alfanumérico? {}' .format(a.isalnum()))
print('Está em maiusculas? {}' .format(a.isupper()))
print('Está em minusculas? {}' .format(a.islower()))



