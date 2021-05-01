"""
def area(l, c):
    a = l*c
    print(f'O terreno de largura {l} e comprimento {c} tem {a}m² de área.')


#PROGRAMA PRINCIPAL
print('Controle de Terrenos')
print('-'*30)
largura = float(input('Informe a largura do terreno: '))
comprimento = float(input('Informe o comprimento do terreno: '))
area(largura, comprimento)



def escreva(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)


#MAIN
texto = str(input('Digite a mensagem desejada: '))
escreva(texto)




from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    if f > i:
        f += 1
    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(0.5)
    print()


#main
contador(1, 10, 1)
contador(10, 1, -2)
print(f'Configure a sua contagem personalizada: ')
inicio = int(input('Informe o inicio desejado: '))
final = int(input('Informe o final desejado: '))
passo = int(input('Informe o passo desejado: '))
contador(inicio, final, passo)




def maior(*num):
    dec = 0
    for c in range(0, len(num)):
        if num[c] > dec:
            dec = num[c]
    print(f'O maior valor é {dec}')


#MAIN
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()


"""
from random import randint
def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 100))

def somaPar(n):
    soma = 0
    for c in range(0, len(n)):
        if n[c] % 2 == 0:
            soma += n[c]
    print(f'A soma de todos os valores pares sorteados é {soma}')


#Main
numeros = list()
sorteia(numeros)
print(f'Os 5 numeros sorteados foram {numeros}')
somaPar(numeros)
