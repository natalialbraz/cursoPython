conjunto = {1, 2, 3, 4}
print(conjunto)
#para adicionar um elemento
conjunto.add(5)
print (conjunto)
#para remover um elemento
conjunto.discard(2)
print(conjunto)

c1= {1,2,3,4,5}
c2= {5,6,7,8,9}
#para fazer a uniao de dois conjuntos
cuniao= c1.union(c2)
print(cuniao)
#para fazer a intersecao
cinter= c1.intersection(c2)
print(cinter)
#para fazer a diferença simetrica(elementos que são únicos os dois conjuntos)
dif= c1.symmetric_difference(c2)
print(dif)


cA = {1,2,3}
cB = {1,2,3,4,5}
#verificar se o conjunto A e um subconjunto de B
#(se esta dentro de B) retorna true ou false
sub = cA.issubset(cB)
print(sub)
#verificar se o conjunto B e um superconjunto de A
#(se engloba A, tem todos os seus elementos
sup = cB.issuperset(cA)
print(sup)

lista= ['cachorro', 'cachorro', 'gato', 'elefante']
#para converter uma lista em conjunto --OBS: a duplicidade e removida
conjAni = set(lista)
print(conjAni)
#para converter um conjunto em lista
listaAni = list(conjAni)
print(listaAni)