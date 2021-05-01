#estruturas compostas: listas parte 1
#é possivel alterar o conteudo (são mutáveis)

"""

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
lanche[3] = 'Picolé'
print(lanche)
#é possivel adicionar novos elementos na lista
#no final:
lanche.append('Cookie')
print(lanche)
#tambem é possivel adicionar entre outros elementos
lanche.insert(1,'lasanha')
print(lanche)
#é possivel apagar elementos
#del lanche[3]
#lanche.pop(3)
#print(lanche)
#existe o metodo remove que vc nao indica o indice e sim o
#valor que deseja eliminar

if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)

#é possivel utilizar uma função chamada list para declarar uma lista
valores = list(range(4, 11))
print(valores)

#para organizar os elementos em ordem crescente
elementos = [8, 2, 5, 4, 9, 3, 0]
elementos.sort()
print(elementos)
#para organizar os elementos ordenados na ordem reversa
elementos.sort(reverse=True)
print(elementos)
#para saber o tamanho da lista (quantidade de indices)
print(len(elementos))



lista1 = [2, 5, 9, 1]
lista1[2] = 3
print(lista1)
lista1.append(65)
#inserindo valores
lista1.insert(2, 22)
lista1.sort()
print(lista1)
print(f'Essa lista tem {len(lista1)} elementos')



l2 = []
l2.append(5)
l2.append(9)
l2.append(4)

for v in l2:
    print(f'{v}...', end='')

#usando for com enumerate para pegar o valor da chave e indice
print('\n')
for c, v in enumerate(l2):
    print(f'Na posição {c} encontrei o valor {v}')

"""
#para declarar a lista como uma entrada digitada pelo usuario
l = []
for cont in range(0,5):
    l.append(int(input('Digite um valor: ')))

print(l)

#observe que ao igualar duas listas, todas as alterações feitas
#em uma serão feitas também na outra, elas estarão ligadas
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#para fazer uma cópia: fazer c receber todos os
#elementos de a
c = a[:]
c[3] = 0
print(f'Lista A: {a}')
print(f'Lista C: {c}')


