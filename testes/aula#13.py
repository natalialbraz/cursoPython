#estrutura de repetição for
#o range ignora o ultimo numero da contagem
#se quiser de 1 a 6 colocar 1 a 7
for c in range(1,7):
    print('OI')
    print(c)
#o formato é
for i in range (6,0,-1):
    print(i)
#para a iteração tirar 1 de i, que começa em 6, fazendo a contagem reversa
#portanto o ultimo argumento do parentese é responsavel pela decrementação
#ou incrementação da variavel de controle
#sendo possivel fazer a contagem de 2 em 2, etc
for n in range(0,11,2):
    print(n)

#é possivel ler um valor e utiliza-lo como parametro em for
d = int(input('Digite um numero: '))
for d in range(0,d+1):
    print(d)
#somando valores
s=0
for f in range(0,4):
    a = int(input('Digite um numero: '))
    s += a #s recebe s + a --> s=s+a
print('O somatório de todos os valores foi {}' .format(s))
