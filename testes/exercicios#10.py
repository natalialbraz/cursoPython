"""
import random
comp = random.randint(0,5)
print('Vou pensar em um numero de 0 a 5 e voce tentará adivinhar!')
usu = int(input('Qual numero eu pensei?'))
if usu==comp:
    print('Você venceu!')
else:
    print('Você perdeu!')
print('Eu pensei no numero {}' .format(comp))


vel = float(input('Qual a velocidade do carro em km?'))
if vel > 80:
    multa= 7*(vel-80)
    print('Voce foi multado em {:.2f} reais' .format(multa))
print('Tenha um bom dia! Dirija com segurança.')


print('Numero par ou impar?')
num = int(input('Digite um numero inteiro:'))
if num%2 == 0:
    print('O numero é par.')
else:
    print('O numero é ímpar.')



d = float(input('Qual é a distância da viagem em km?'))
if d<= 200:
    passagem = d*0.5
else:
    passagem = d*0.45
print('O preço da passagem será: {:.2f} reais' .format(passagem))



print('Analisando se o ano é bissexto')
ano = int(input('Que ano quer analisar?'))
if ano%4 == 0:
    print('O ano {} é bissexto!' .format(ano))
else:
    print('O ano {} não é bissexto!' .format(ano))



n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite mais um numero:'))
maior = n1
menor = n1
if n2>maior and n2>n3:
    maior=n2
if n3>maior and n3>n2:
    maior=n3
print('O maior numero é: {}' .format(maior))
if n2<menor and n2<n3:
    menor = n2
if n3<menor and n3<n2:
    menor = n3
print('O menor numero é: {}' .format(menor))

"""


print('Cálculo do aumento do seu salário')
salario = float(input('Qual o valor do seu salario atual?'))
if salario>1250.00:
    novosal = salario+(salario*10)/100
else:
    novosal = salario+(salario*15)/100
print('Seu novo salario é {:.2f} reais' .format(novosal))



"""
r1 = int(input('Qual o primeiro lado do triangulo?'))
r2 = int(input('Qual o segundo lado do triangulo?'))
r3 = int(input('Qual o terceiro lado do triangulo?'))
if (r1+r2)>r3 and (r1+r3>r2) and (r2+r3>r1):
    print('As retas podem formar um triangulo')
else:
    print('As retas não podem formar um trinagulo')
"""




