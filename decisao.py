"""
exercicio 1
n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
if n1>n2:
    print('O maior numero e: {} ' .format(n1))
else:
    print('O maior numero e: {}  ' .format(n2))
"""
"""
exercicio 2
valor = int(input('Informe um numero: '))
if valor>0:
    print('O valor informado e positivo.')
elif valor==0:
    print('O valor e igual a zero.')
else:
    print('O valor informado e negativo.')
"""
"""
exercicio 4
letra = str(input('Digite uma letra: '))
if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print('A letra e vogal.')
else:
    print('A letra e consoante.')
"""
"""
exercicio 5
n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
media = (n1+n2)/2
if media==10:
        print('APROVADO COM DISTINCAO')
elif media>=7:
    print('APROVADO')
else:
    print('REPROVADO')
"""
"""
exercicio 8
p1 = float(input('Informe o preco do produto:'))
p2 = float(input('Informe o preco do produto:'))
p3 = float(input('Informe o preco do produto:'))
if p1<p2 and p1<p3:
    print('Voce deve comprar o produto 1, que custa {} reais' .format(p1))
elif p2<p1 and p2<p3:
    print('Voce deve comprar o produto 2, que custa {} reais' .format(p2))
else:
    print('Voce deve comprar o produto 3, que custa {} reais' .format(p3))
"""
"""
exercicio 11
salario = float(input('Informe seu salario atual:'))
if salario<=280.00:
    percentual = 20
    aumento= (salario*20)/100
    recebe= salario+aumento
elif salario>280.00 and salario<700.00:
    percentual = 15
    aumento= (salario*15)/100
    recebe = salario + aumento
elif salario>=700.00 and salario<1500:
    percentual = 10
    aumento= (salario*10)/100
    recebe = salario + aumento
else:
    percentual = 5
    aumento= (salario*5)/100
    recebe = salario + aumento
print('O salario antes do ajuste era {} reais' .format(salario))
print('O percentual de aumento aplicado e {}% ' .format(percentual))
print('O valor do aumento e {} reais' .format(aumento))
print('O novo salario e {} reais' .format(recebe))
"""
""" 
exercicio 14 (erro)
n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
media = (n1+n2)/2
if media>9 and media>10:
    c = 'A'
elif media<=9 and media>7.5:
    c = 'B'
elif media<=7.5 and media>6.0:
    c = 'C'
elif media<=6 and media>4.0:
    c = 'D'
else:
    c = 'E'
if c== 'A' or c== 'B' or c== 'C'
    print('APROVADO')
else:
    print('REPROVADO')
"""
"""
exercicio 15
lado1 = int(input('informe o primeiro lado do triangulo:'))
lado2 = int(input('informe o segundo lado do triangulo:'))
lado3 = int(input('informe o terceiro lado do triangulo'))
if lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1:
    print('Os valores informados podem ser triangulos!')
    if lado1==lado2 and lado2==lado3:
        print('Triangulo equilatero')
    elif lado1==lado2 or lado2==lado3 or lado1==lado3:
        print('Triangulo Isosceles')
    else:
        print('Triangulo Escaleno')

else:
    print('Os  valores informados nao podem ser triangulos!')
"""
"""
exercicio 21(erro)
saque= int(input('informe o valor(entre 10 a 600 reais) que deseja sacar (notas disponiveis: 1-5-10-50-100): '))
ncem= saque/100
r1= saque-(ncem*100)
if r1>0:
    ncinq= r1/50
    r2 = r1-(ncinq*50)
    if r2>0:
        ndez= r2/10
        r3= r2-(ndez*10)
        if r3>0:
            ncinco= r3/5
            r4 = r3-(ncinco*5)
            num= r4/1
print('Serao fornecidas {} notas de 100 reais, {} notas de 50 reais, {} notas de 10 reais, {} notas de cinco reais, {} notas de um real' .format(ncem,ncinq,ndez,ncinco,num))
"""
