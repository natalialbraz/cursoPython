#PROGRAMA PRINCIPAL
import moeda
p = float(input('Digite o preço: R$'))
print(f'Aumentando 10%, temos {moeda.m(moeda.aumentar(p, 10))}')
print(f'Diminuindo 10%, temos {moeda.m(moeda.diminuir(p, 10))}')
print(f'A metade de {moeda.m(p)} é {moeda.m(moeda.metade(p))}')
print(f'O dobro de {moeda.m(p)} é {moeda.m(moeda.dobro(p))}')

