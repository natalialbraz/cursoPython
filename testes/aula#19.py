#variaveis compostas: dicionários
"""
são semelhantes as tuplas e listas mas permitem ter
indices literais
como declarar dicionarios

dados = dict()
d = {}

#podemos declarar informando o identificador e o valor
#separados por 2 pontos
cad = {'nome':'Pedro', 'idade':25}
print(cad['nome'])
print(cad['idade'])
#como adicionar um elemento
cad['sexo']= 'M'
#podemos deletar
del cad['idade']
#é importante saber diferenciar o que é valor, chave e item
filme = {'título':'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }
#valores
print(filme.values())
#chaves
print(filme.keys())
#se quiser cada item, tanto os valores quanto chaves
print(filme.items())

#percorrendo laços
for k, v in filme.items():
    print(f'O {k} é {v}')

#é possivel juntas tuplas, lista e dicionários
#por exemplo, é possivel criar uma lista com um dicionário dentro


pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade':22}
#diferente das outras estruturas, usamos as chaves nominais
#para mostrar o elemento desejado
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for i in pessoas.items():
    print(i)
#é possivel alterar o dados - trocando Gustavo por Leandro
pessoas['nome'] = 'Leandro'


#criando um dicionario dentro de uma lista
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
#dentro da lista temos um primeiro elemnto, que é um dicionario
#estado1 e um segundo elemento estado2
#se quiser mostrar o prmimeiro elemtno da lista
print(brasil[0])
#se quiser mostrat o segundo elemento com a chave uf
print(brasil[0]['uf'])

"""
#fazendo uma copia do elemento sem usar fatiamento
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

