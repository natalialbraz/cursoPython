"""
from math import trunc
n = float(input('Informe um numero:'))
ninteiro = trunc(n)
print('O numero digitado foi {} e sua porção inteira e {}'.format(n, ninteiro))


#calculando a hipotenusa utilizando raiz quadrada
from math import sqrt
c1 = int(input('informe o comprimento do cateto oposto'))
c2 = int(input('informe o comprimento do cateto adjacente:'))
aux = c1**2 + c2**2
hip = sqrt(aux)
print('O comprimento da hipotenusa é: {}' .format(hip))


#existe uma função na biblioteca math para calcular a hipotenusa
import math
c1 = int(input('informe o comprimento do cateto oposto'))
c2 = int(input('informe o comprimento do cateto adjacente:'))
hip = math.hypot(c1, c2)
print('O comprimento da hipotenusa é: {}' .format(hip))


import math
angulo = int(input('Digite o valor do angulo:'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O seno e {:.2f}\n o cosseno e {:.2f}\n e a tangente e {:.2f}' .format(seno,cosseno,tangente))



import random
n1 = str(input('Digite o nome do aluno:'))
n2 = str(input('Digite o nome do aluno:'))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
#para definir a ordem de apresentação random.shuffle(lista)
print('O aluno {} foi escolhido para apagar o quadro' .format(escolhido))
random.shuffle(lista)
print('A ordem de apresentação será {}' .format(lista))
"""

import pygame
pygame.init()
pygame.mixer.music.load('nomedoarquivomp3')
pygame.mixer.music.play()
#para esperar a musica terminar de tocar para encerrar o programa
pygame.event.wait()