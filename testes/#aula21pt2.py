"""
def somar(a, b, c):
    s = a+b+c
    print(f'A soma vale {s}')

#PRINCIPAL
somar(3, 2, 5)
somar(8, 4)
se a quantidade de parametros normais e formais forem diferentes
o programa dara erro, utilizamos entao o conceito de parametros
opcionais

def somar(a, b, c=0):  #se nao receber c, ele valera 0
    #é possivel colocar todos os parametros como opcional
    s = a+b+c
    print(f'A soma vale {s}')

#PRINCIPAL
somar(3, 2, 5)
somar(8, 4)



escopo é o local onde uma variavel vai existir e um local onde
ela nao vai mais existir
def teste():
    print(f'Na função teste, n vale {n}')


#main
n = 2 #mesmo n sendo definido no programa principal irá funcionar
#no programa inteiro, chamamos isso de ESCOPO GLOBAL
print(f'No programa principal, n vale {n}')
teste()


def teste():
    x = 8 #é uma variavel local, só funciona nessa area
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#MAIN
n = 2 #variavel global
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale{x}') #nesse caso ocorrerá
#um erro, pois x é uma variavel local, entao nao funciona no
#programa principal

@@@@@@@@@ ATENÇÃO @@@@@@@@@
caso defina a variavel "a" no programa principal(escopo global)
e na definição da função(escopo local) faça por exemplo a= 20
NAO SE ENGANE
vc na estará redefinindo a variavael global "a", na verdade
estará criando uma nova variavel local "a"
caso queira utilizar o valor de a global faça



def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


#PRINCIPAL
a = 5
teste(a)
print(f'A fora vale {a}')


#retornando valores
#é util quando queremos apenas o resultado ou um print personalizado

def soma(a=0, b=0, c=0):
    s = a + b +c
    return s

#principal
r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')



def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

#principal
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

"""

#tambem é possivel retornar valores logicos, strings, listas,
#dicionarios, tuplas
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')






