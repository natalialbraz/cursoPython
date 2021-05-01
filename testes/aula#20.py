#funçoes pt1
"""
def soma(a, b):
    s = a + b
    print(s)


#programa principal
#passando os seguintes parametros
soma(4, 5)
soma(8, 9)
soma(2, 1)

#empacotamento de parametros
#o asterisco é pq nao sabemos a quantidade de parametros que serao
#passados, então jogamos tudo em "num"
def contador(*num):
    #print(num)
#uma tupla é criada com todos valores
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')


#PROGRAMA PRINCIPAL
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

"""
#trabalhando com listas
#nesse caso nao é necessário empacotar e desempacotar pois podemos
#passar a lista, funções aceitam listas como parametros
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#MAIN
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)


