variavel1  = "ola"
variavel2 = "mundo"
concatenacao = variavel1+ " " +variavel2
print (concatenacao)
"""
para descobir o tamanho da string usa a funcao len(string)
"""
tamanho = len(concatenacao)
print(tamanho)
"""
é possivel navegar pela string atraves dos indices
"""
print(variavel1[2])
"""
é possivel imprimir uma parte da string indicando o indice inicial e final
"""
print(concatenacao[0:5])
"""
em python strings sao objetos, podendo aplicar metodos a elas
por exemplo alterar a caixa: 
minusculo-> lower
maiusculo-> upper
"""
seq= "ASDFGASDFG"
seq2 = "qwertqwert"
print(seq.lower())
print(seq2.upper())
"""
dessa maneira altera-se apena a forma como a variavel 
e impressa
para alterar a variavel de fato, deve-se aplicar a variavel
"""
seq = seq.lower()
print(seq)
"""
a funcao strip remove caracteres especiais do inicio ou
final de uma string
ja a funcao split converete uma string a uma lista
"""
f = "O rato roeu a roupa do rei de Roma"
lista = f.split()
print(lista)
"""
fazendo por exemplo lista = f.split("r")
a lista quebrara sempre na letra r e essa nao aparecera

para fazer busca em uma sttring utiliza-se o metodo find
"""
busca = f.find("rei")
print(busca)

# o metodo replace substitui partes de uma string
f = f.replace("rei", "rainha")
f = f.replace("do", "da")
print(f)

