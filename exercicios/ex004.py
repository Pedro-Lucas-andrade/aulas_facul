nome = input('Digite o nome do vendedor: ')
salario = float(input('Digite o salário do vendedor {}: '.format(nome)))
vendas = float(input('Digite o valor toral de vendas do vendedor {}: '.format(nome)))
comissao = 0.15*salario
sfinal = salario + comissao
print('O vendedor {} tem um salário fixo de {} R$, realizou {} R$ em vendas, ganhou uma comissão de {} R$, e seu salário final foi de {} R$'.format(nome, salario, vendas, comissao, sfinal))
