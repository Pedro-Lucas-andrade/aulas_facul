salario = 1000
aumento= float(1,5/100)
ano_atual = int(input('Digite o ano atual: '))
tempo= int(ano_atual - 2015)
novo_aumento = aumento + (tempo - 1)*2

novo_salario = salario*novo_aumento
print('seu salario é: {}'.format(novo_salario))
