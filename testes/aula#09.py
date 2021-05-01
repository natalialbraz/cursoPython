#manipulando cadeias de texto
frase = 'curso em video python'
print(frase[9])
print(frase[9:13])
#para ir do 9 ao 21 de dois em dois
print(frase[9:21:2])
#para começar no inicio e terminar no lugar indicado
print(frase[:5])
#indicando o inicio sem indicar o final
print(frase[15:])
#para começar no local indicando de 3 em 3 sem determinar o final
print(frase[9::3])

#analisando uma string
#para saber o comprimento da frase(qtde de caracteres)
print(len(frase))
#para contar quantas vezes determinado caracter aparece na frase
print(frase.count('o'))
#para selecionar o inicio e fim de onde sera a contagem
print(frase.count('o',0,13))
f = ('a garrafa ao lado da cama')
#para indicar onde começa palavra procurada
print(f.find('ama'))
#para verificar se existe certa palavra dentro de uma string
print('curso' in f)

#transformação
#substituindo uma palavra por outra
print(f.replace('cama', 'mesa'))
#deixando a frase em maisculas ou minusculas
print(f.upper())
print(f.lower())
#para jogar todos os caracteres para minusculo e apenas o primeiro da frase maiusculo
print(f.capitalize())
#para deixar todas as palavras com a primeira letra maiuscula
print(f.title())
#para eliminar espaços inuteis no inicio e final da string
print(f.strip())
#para remover espaços apenas do final:r = rigth (direita)
print(f.rstrip())
#para remover espaços apenas do inicio:l = left (esquerda)
print(f.lstrip())


#divisao de strings
#para dividir a string de acordo com os espaços
print(f.split())
#para separar os caracteres antes separados por espaços, agora por hifens
print('-'.join(f))