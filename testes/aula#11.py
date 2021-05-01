#cores no terminal
"""
codigo ANSI escape sequence - vamos utiliza-lo para cores
ele começa com o contra barra(\) e codigo na frente
existe uma faixa para o codigo das cores, o que funciona melhor
em python é a 033 e
EXEMPLO:
\033[CODIGODACORm
esse codigo da cor pode ser preenchido com até 3 coisas
\033[style;text;backm
*os codigos para estilo são:
0 -> none(sem estilo)
1 -> bold(negrito)
4 -> underline(sublinhado)
7 -> negative(config do fundo vai pra letra e config da letra vai pra fundo
*os codigos para cor da letra são:
30 -> branco
31 -> vermelho
32 -> verde
33 -> amarelo
34 -> azul
35 -> lilas
36 -> verde agua
37 -> cinza
*os codigos para cores de fundo são:
40 -> branco
41 -> vermelhor
42 -> verde
43 -> amarelo
44 -> azul
45 -> lilas
46 -> verde agua
47 -> cinza

print('\033[0;30;41m TESTANDO')
print('\033[4;33;44m Ola mundo')
print('\033[0;35;43m usando cores')
print('\033[0;30;42m colorindo')
print('\033[m voltando ao normal')
print('\033[7;30m inverti')

"""
#alterando apenas onde tem texto sem alterar a linha toda
print('\033[4;30;45m hora da pratica\033[m')

a = 2
b = 10
#print('Os valores são \033[32m{}\033[m e \033[36m{}' .format(a,b))

#criando variaveis de cores prontas para uso
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'}
nome = 'ana'
sobre = 'flavia'
print('O seu nome é {}{}{} e seu sobrenome é {}{}{}. OK?' .format(cores['amarelo'], nome, cores['limpa'], cores['azul'], sobre, cores['limpa']))
