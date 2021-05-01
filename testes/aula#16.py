#variaveis compostas
#tuplas
"""
as tuplas são imutáveis: uma vez definida permanecerá asssim
até o final do programa


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print('Eu vou comer', end='')
#dessa forma nao é possivel mostrar a posição
for comida in lanche:
    print(f' {comida},' ,end="")
#outra maneira de usar o for

print('\n')
for c in range(0, len(lanche)):
    print(lanche[c])


"""
#tambem é possivel saber a posição do item das duas maneiras
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# ele nao altera a tupla, apenas coloca em ordem
print(sorted(lanche))

#a soma de duas tuplas funciona como uma concatenação, nesse
#caso então a ordem dos fatores altera o resultado

a = (2, 5, 4)
b = (5, 8, 1, 2)
d = b + a
c = a + b
print(c)
print(d)

#para contar quantas vezes aparece determinado elemento
print(c.count(5))

#para saber a posição da primeiera ocorrencia de determinado elemento
print(d.index(2))
#dada a primeira voce pode verificar outra ocorrencia após a posição da primeira
print(d.index(2, 4))

#em uma tupla podemos escrever dados de diferentes tipos
pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
#a unica coisa que podemos fazer com uma tupla é apaga-la
del(pessoa)
print(pessoa)



