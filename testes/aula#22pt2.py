#pacotes
"""
util quando os modulos ficam muito grandes
pacotes é a junção de modulos separados por assunto
é uma pasta que contem modulos
dentro do python todo arquivo pode ser considerado um modulo
e toda pasta pode ser considerada um pacote
@@@ ATENÇÃO @@@
existe uma sintaxe para nomes de arquivos dentro de pacotes

-cria-se o pacote. ex: pacotinho-->PROJETO:new python package
podemos criar pacotes dentro de pacotes
a cada pacote criado cria-se automaticamente um arquivo vazio
com o nome __init__.py

para usa-lo é simples
import pacotinho
ou para usar um pacote dentro do pacote
from pacotinho import numeros






"""
#principal

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)} ')
print(f'O triplo de {num} é {uteis.triplo(num)}')