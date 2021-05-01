#funções pt2
"""
assuntos: interactive help, docstrings, argumentos opcionais,
escopo de variaveis, funçoes com retorno de resultados
usando a ajuda interativa
abrir o python console perto do terminal e digitar help()
docstrings são strings de documentação, todas as funcionalidade do
python possuem uma
def contador(i, f ,p):  #parametros normais
    comandos
#principal
contador(2, 10, 2)   #parametros formais
existe uma copia do parametos formais para os normais feita de
forma automatica
ao utilizar uma biblioteca ja criada por outra pessoas e voce
nao sabe o que são os parametros, ou como a função funciona
podemos criar entao uma docstring qye consiste em escrever o que
deseja entre 3 aspas duplas abrindo e fechando
ao solicitar o help(contador) no codigo, a docstring será exibida
DOCSTRING manual a ser exibido durante qualquer ajuda interativa
"""

def contador(i, f, p):
    """

    faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


contador(2, 10, 2)
help(contador)





