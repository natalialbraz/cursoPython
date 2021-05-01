#aprovando empréstimo
"""
valor = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Voce deseja pagar em quantos anos? '))
meses = anos*12
mensal = valor/meses
print('Para pagar uma casa de {:.2f} reais em {} anos, a prestação será de {} reais' .format(valor, anos, mensal))
if mensal > (salario*30)/100:
    print('Empréstimo negado pois a mensalidade excede 30% do seu salário')
else:
    print('Empréstimo aprovado' .format(mensal))


num = int(input('Digite um numero inteiro:'))
op = int(input('Escolha a base de conversão: 1- binario 2- octal 3-hexadecimal: '))
if op == 1:
    conv = bin(num)
    print('{} convertido em binário é {}' .format(num,conv))
elif op==2:
    conv = oct(num)
    print('{} convertido em octal é {}' .format(num,conv))
else:
    conv = hex(num)
    print('{} convertido em hexadecimal é {}' .format(num,conv))


n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero:'))
if n1>n2:
    print('O primeiro valor é maior')
elif n2>n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')


#alistamento militar
#podemos importar uma biblioteca de data e tempo para nos informar em que ano estamos
from datetime import date
atual = date.today().year
nasceu = int(input('Em qual ano você nasceu? '))
idade = atual-nasceu
if idade<18:
    falta = 18-idade
    print('Você ainda vai se alistar. Faltam {} anos' .format(falta))
elif idade==18:
    print('Está na hora de se alistar')
else:
    passou = idade-18
    print('Você passou {} anos do prazo de se alistar' .format(passou))


n1 = float(input('Informe a nota da primeira prova: '))
n2 = float(input('Informe a nota da segunda prova: '))
media = (n1+n2)/2
print('Tirando {} na P1 e {} na P2, a media do aluno é {} pontos' .format(n1, n2, media))

if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')


#classificando atletas
from datetime import date
nasceu = int(input('Em qual ano você nasceu? '))
atual = date.today().year
idade = atual-nasceu
print('Sua categoria é: ')
if idade <= 9:
    print('MIRIM')
elif idade>9 and idade<=14:
    print('INFANTIL')
elif idade> 14 and idade<=19:
    print('JUNIOR')
elif idade>19 and idade<=25:
    print('SÊNIOR')
elif idade >25:
    print('MASTER')


l1 = int(input('Informe um lado do triangulo:'))
l2 = int(input('Informe outro lado do triangulo: '))
l3 = int(input('Informe o terceiro lado do triangulo: '))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print('esses lados formam um triangulo')
    if l1 == l2 and l2 == l3:
        print('equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('isósceles')
    elif l1 != l2 and l1 != l3 and l2!=l3:
        print('escaleno')
else:
    print('Esses lados nao satisfazem a condição de existencia de um triangulo')


#IMC
peso = float(input('Qual é seu peso?(kg) '))
altura = float(input('Qual é sua altura?(m) '))

imc = peso/(altura**2)
print('Seu IMC é {:.1f} ' .format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')


preço = float(input('Qual é o preço do produto? '))
print('Informe o meio de pagamento')
print('1- a vista no dinheiro ou cheque')
print('2- a vista no cartão')
print('3- em ate 2 vezes no cartão')
print('4- em 3 vezes ou mais no cartão')
pag = int(input('Opção: '))
if pag == 1:
    valor = preço-(preço*10)/100
elif pag == 2:
    valor = preço-(preço*5)/100
elif pag == 3:
    opç = int(input('Em quantas vezes você deseja parcelar? '))
    valor = preço
    parcela = valor/opç
    print('Sua compra será paga em {}x de {:.2f} reais' .format(opç, parcela))
elif pag == 4:
    opç = int(input('Em quantas vezes você deseja parcelar? '))
    valor = preço + (preço * 20 / 100)
    parcela = valor / opç
    print('Sua compra será divida em {}x de {:.2f} reais' .format(opç, parcela))
print('O  valor total a ser pago é {:.2f} ' .format(valor))

"""
#game jokenpô
import random
itens = ('Pedra', 'Papel', 'Tesoura')
print('Escolha:\n 0-Pedra 1-Papel 2-Tesoura')
computador = random.randint(0,2)
voce = int(input('Qual é a sua jogada? '))
print('Você jogou {}' .format(itens[voce]))
print('O computador jogou {}' .format(itens[computador]))

if computador == 0:
    if voce == 0:
        print('Empataram!')
    elif voce == 1:
        print('Você ganhou!')
    elif voce == 2:
        print('Você perdeu!')
elif computador == 1:
    if voce == 0:
        print('VocÊ perdeu!')
    elif voce == 1:
        print('Empataram!')
    elif voce == 2:
        print('Você ganhou!')
elif computador ==2:
    if voce == 0:
        print('Você ganhou!')
    elif voce == 1:
        print('Você perdeu!')
    elif voce == 2:
        print('Empataram!')

