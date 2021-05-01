"""
nome = str(input('Digite o seu nome completo:'))
print('Analisando seu nome:')
print('Seu nome em maiusculas é {}' .format(nome.upper()))
print('Seu nome em minusculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))


n = int(input('Digite um numero situado entre 0 e 9999: '))
u = n//1 % 10
d = n//10 %10
c = n//100 %10
m = n//1000 %10
print('Analisando o numero {}' .format(n))
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))


n = str(input('Digite o nome da cidade:'))
print(n[:5].upper() == 'SANTO')


print('Procurando uma string dentro de outra')
nome = str(input('Digite seu nome:'))
print('SILVA' in nome.upper())


f = str(input('Digite uma frase:')).upper()
print('A letra A aparece {} vezes na frase' .format(f.count('A')))
print('A letra A aparece pela primeira vez na posição {}' .format(f.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}' .format(f.rfind('A')+1))
#coloca-se o +1 para adequar a posição ao usuario, já que a contagem da maquina começa em 0
#o rfind começará a busca pela direita

"""
nome = str(input('Digite seu nome completo:'))
n = nome.split()

print('O seu primeiro nome é {}' .format(n[0]))
print('O seu último nome é {}' .format(n[len(n)-1]))


