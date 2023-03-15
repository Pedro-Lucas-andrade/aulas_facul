produto = input('Digite o nome do produto: ')
custo = float(input('Digite o custo do produto: '))
percentual = float(input('Digite o acrescimo em porcetagem(%)'))
valor_de_venda = custo + percentual/100*custo
print('O valor que o {} terá é de {} R$'.format(produto, valor_de_venda))