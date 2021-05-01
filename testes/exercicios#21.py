"""
from datetime import date
def voto(a):
    atual = date.today().year
    idade = atual - a
    if idade < 16:
        return f'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'VOTO OPCIONAL'
    else:
        return f'VOTO OBRIGATORIO'


#PRINCIPAL
ano = int(input('Informe seu ano de nascimento: '))
print(f'Situação eleitoral {voto(ano)}')





def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


#main
numero = int(input('Informe o numero que deseja calcular o fatorial: '))
print(f'Fatorial de {numero} = {fatorial(numero)}')


def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato.')


#main
nome = str(input('Nome do jogador: '))
gols =str(input('Quantidade de gols feitos: '))
if gols.isnumeric():
    gols = int(gols)
else:
    print('Carectere inválido. Favor digitar um numero inteiro.')
    gols = str(input('Quantidade de gols feitos: '))
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)




def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'ERRO! Digite um numero válido')
        if ok:
            break
    return valor


#main
n = leiaint(f'Digite um numero; ')
print(f'Você acabou de digitar o numero {n}')





def notas(*n, sit=False):
    ###
    --> função para analisar notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar  a situação
    :return: dicionario com varias informações sobre a situação da turma
    ###
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

#main
resp = notas(10, 5.5, 2.5, 9, 8.5, sit=True)
print(resp)
help(notas)


"""

def ajuda(c):
    help(c)



#main
comando = ''
while True:
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)












