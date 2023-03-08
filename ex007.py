cotacao = float(input('Digite a cotação do dolár: '))
dolar = float(input('Digite o valor que deseja converter (R$ ➝ U$)'))
real = dolar*cotacao
print('{} U$ em R$ é {}R$'.format(dolar, real))
