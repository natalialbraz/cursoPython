"""
lista = [1,2,3,4,5,6]
lista_animal = ["gato", "cachorro", "lebre"]
print(lista_animal[1]) #imprime o elemento que esta na posicao 1
nova = lista_animal*3
print(nova)   #multiplica a lista
#para verificar se um elemento se encontra na lista:
if "lobo" in lista_animal:
    print ("existe um lobo na lista")
else:
    print("nao existe um lobo na lista")

#para adicionar um elemento a lista:
lista_animal.append("lobo")
print(lista_animal)

#para retirar o ultimo elemento da lista
lista_animal.pop()
#para retirar um elemento especifico
lista_animal.pop(0)
print(lista_animal)
# e possivel retirar tambem atraves de um nome especifico
lista_animal.remove("lebre")
"""
lista1 = [34, 6, 23,12]
lista2 = ["arara", "leao", "camelo", "iguana"]

lista1.sort()
lista2.sort()
print(lista1)
print(lista2)
#sort ordena a lista do ultimo elemento para o primeiro

lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
# reverse ordena a lista em ordem decrescente

tupla = (1, 10, 12, 14)
print(tupla[0])