n1 = float(input('Digite sua 1º nota: '))
n2 = float(input('Digite sua 2º nota: '))
n3 = float(input('Digite sua 3º nota: '))

media = (n1+n2+n3)/3

print('Sua média é {}'.format(media))

if( media < 3):
    print('REPROVADO')
elif ( media >=3 and media <7 ):
    print('EXAME')
elif ( media >= 7 and media <= 10):
    print('APROVADO')