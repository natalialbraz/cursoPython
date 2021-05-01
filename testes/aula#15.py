#interrompendo repetições while
n= s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {} ' .format(s))
#OBS: python agora aceita as fstrings, veja
print(f'A soma vale {s:.2f}')