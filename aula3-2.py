"""
a = int(input('entre com um valor:'))
b = int(input('entre com outro valor:'))

resto_a = a%2
resto_b = b%2
if resto_a==0 or resto_b==0:
    print('foi digitado um numero par')
else:
    print('nenhum numero par foi digitado')
"""
n1 = int(input('Digite a primeira nota do aluno'))
n2 = int(input('Digite a segunda nota do aluno:'))
n3 = int(input('Digite a terceira nota do aluno:'))
n4 = int(input('Digite a segunda nota do aluno:'))
media = (n1+n2+n3+n4)/4
print('a media do aluno e {}' .format(media))
if media>10:
    print('a media do aluno e {}'.format(media))
else:
    print('alguma nota foi informada errada')
    