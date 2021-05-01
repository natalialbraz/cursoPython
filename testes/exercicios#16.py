"""
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero de 0 a 20: '))
print(f'{n} por extenso é {tupla[n]}')

#outra forma

tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente novamente.')
print('Voce digitou o numero {tupla[n]}')


times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Os 5 primeiros colocados do CBF são {times[0:5]}')
#print(f'Os ultimos 4 colocados são {times[16:]}')
#ou tambem
print(f'Os ultimos 4 colocados são {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O Chapecoense está na posição {times.index("Chapecoense")}')




import random

n = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print('Os numeros gerados foram: ', end="")
menor = 100000000000
maior = 0
for c in range(0, len(n)):
    print(f'{n[c]}' ,end=' ' )
    if n[c] < menor:
        menor = n[c]
    if n[c] > maior:
        maior = n[c]

print('\n')
# ou podemos usar um metodo para encontrar o maior e menor
# valor em uma tupla
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')

print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')



num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'O valor 9 apareceu {num.count(9)} vezes ')
print(f'O valor 3 foi digitado pela primeira vez na posição {num.index(3)}')
print('Os valores pares foram: ')
for c in
range(0,len(num)):
       if num[c] % 2 == 0:
              print(f'{num[c]} ',end='')



listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}' ,end='')
    else:
        print(f'R${listagem[pos]:>10.2f}')

"""
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p} temos ' ,end = '')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
