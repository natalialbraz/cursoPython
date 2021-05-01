"""
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1+n2
m = n1*n2
sub = n1-n2
div = n1/n2
p = n1**n2
resto = n1%n2
di = n1//n2
#para formatar a impressao de acordo com o numero de casas desejados
print('A divisao e {:.3f}' .format(div))
#para imprimir os dois prints na mesma linha colocar no final: ,end= ' '
print('A soma e {}, a subtração e {} e a potenciação e {}' .format(s, sub, p) , end=' ')
#para quebrar a linha no meio do print coloca \n
print('A multiplicação e {} \n o resto e {} \ne a divisao inteira e {}' .format(m, resto, di))

num = int(input('Digite um numero inteiro: '))
an = num-1
su = num+1
print('O seu antecessor e {} e o sucessor e {}' .format(an, su))
dobro = 2*num
triplo= 3*num
raiz = num**(1/2)
print('O dobro e {} \n O triplo e {} \n A raiz do numero e {}' .format(dobro,triplo,raiz))

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A nota media do aluno e {} ' .format(media))


metros = float(input('Informe o valor em metros:'))
cm = metros*100
mm = metros*1000
print('{} metros sao {} centimetros e {} milimetros' .format(metros,cm, mm))


n = int(input('Informe um numero inteiro: '))
m0 = n*0
m1 = n*1
m2 = n*2
m3 = n*3
m4 = n*4
m5 = n*5
m6 = n*6
m7 = n*7
m8 = n*8
m9 = n*9
m10 = n*10
print('Tabuada do {}: \n {}x0 = {}\n {}x1 = {}\n {}x2 = {}' .format(n,n,m0,n,m1,n,m2))
print(' {}x3 = {}\n {}x4 = {}\n {}x5 = {}\n {}x6 = {}' .format(n, m3, n, m4, n, m5, n, m6))
print(' {}x7 = {}\n {}x8 = {}\n {}x9 = {}\n {}x10 = {}' .format(n, m7, n, m8, n, m9, n, m10))


din = float(input('Quantos reais voce tem?'))
dolar = din/3.27
print('Com {:.2f} reais voce pode comprar {:.2f} dolares' .format(din, dolar))


l = float(input('Informe a largura da parede em metros:'))
a = float(input('Informe a altura da parede em metros:'))
a = l*a
qtd = a/2
print('Serao necessarios {} litros de tinta para pintar a parede.' .format(qtd))



preco = float(input('qual o preco do produto?'))
novop = preco-(preco*5/100)
print('O novo preço do produto com desconto de 5% é {:.2f} reais' .format(novop))


salario = float(input('Digite seu salario:'))
novos = salario+(salario*15/100)
print('O seu novo salario, com aumento de 15% é: {:.2f} reais' .format(novos))

"""
km = float(input('Informe a quantidade de km rodados:'))
dias = int(input('Informe a quantidade de dias que o carro foi alugado:'))
preco = 60*dias+0.15*km
print('O preço a pagar é {:.2f} reais' .format(preco))
