n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

aux = n1
n1 = n2
n2 = aux

print('invertendo...')
print('n1: {}, n2: {}'.format(n1, n2))