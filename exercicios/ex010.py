produto = input('Digite o nome do produto: ')
valor = float(input('Digite o valor do produto(R$): '))
parcelas = valor/5
print('O valor das parcelas do produto {} serão de {} R$'.format(produto, parcelas))