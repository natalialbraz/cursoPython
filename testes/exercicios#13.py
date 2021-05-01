"""
#contagem regressiva
import time
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print('ESTOURO')


#numeros pares entre 1 e 50
for c in range(2,51,2):
    print(c)


#soma impares multiplos de 3
s=0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c


print('A soma dos numeros pares multiplos de 3 situados entre 1 e 500 é {}' .format(s))


#tabuada
n = int(input('Escolha um numero de 0 a 10: '))
print('Multiplicação de {}:' .format(n))
for c in range (0, 11):
    mult = c*n
    print('{}x{} = {}' .format(c, n, mult))
print('Divisão de {}:' .format(n))
for c in range(1, 11):
    div = n/c
    print('{}/{} = {} ' .format(n, c, div))
print('Soma de {}' .format(n))
for c in range(0, 11):
    s = n + c
    print('{}+{} = {}' .format(n, c, s))
print('Subtração de {}:' .format(n))
for c in range(0, 11):
    sub = n-c
    print('{}-{} = {}' .format(n, c, sub))


#soma dos pares
sp = 0
for c in range(1,7):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        sp = sp + n
print('A soma de numeros pares é {}' .format(sp))


#progressão aritmetica
t1 = int(input('Informe o primeiro termo: '))
r = int(input('Qual é a razão da PA? '))

print('Os 10 primeiros termos são:')
for c in range(0,10):
    a = t1 + c * r
    print(a)


#numeros primos
n = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, n+1):
    if n % c ==0:
        tot = tot + 1
if tot == 2:
    print('É um numero primo')
else:
    print('Não é um numero primo')


#detector de palindromo
frase = str(input('Digite uma frase: ')).upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[i]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')


from datetime import date
atual = date.today().year
cmaior = 0
cmenor =0
for c in range(0, 7):
    ano = int(input('Você nasceu em que ano? '))
    idade = atual - ano
    if idade >= 18:
        cmaior = cmaior + 1
    else:
        cmenor = cmenor + 1
print('{} pessoas já são maiores de idade' .format(cmaior))
print('{} pessoas são menores de idade' .format(cmenor))


maior = 0
menor = 10000000000000000
for c in range(0, 5):
    peso = float(input('Qual é seu peso?(kg) '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O menor peso é: {} kg' .format(menor))
print('O maior peso é {} kg' .format(maior))

"""

somai = 0
somaf = 0
maior = 0
velho= ''
for c in range (0,4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual é o seu sexo? '))
    somai += idade
    if sexo == 'feminino' and idade <20:
        somaf += 1
    if sexo == 'masculino' and idade>maior:
        velho = nome
media = somai/4
print('A media de idade do grupo é {:.2f} anos' .format(media))
print('O nome do homem mais velho é {}' .format(velho))
print('{} mulheres tem menos de 20 anos' .format(somaf))










