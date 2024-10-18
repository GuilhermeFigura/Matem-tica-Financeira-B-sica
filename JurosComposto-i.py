""" Esse programa irá encontrar taxa de juros mensal de juros com base nas informações solicitadas. """

pv = float(input(f'Qual o valor inicial do investimento? R$ '))
fv = float(input(f'Qual o valor do montante que deseja? R$ '))
n = int(input(f'Qual o número de dias corridos do investimento? '))

i = ((fv / pv) ** (30 / n) - 1) * 100

print(f'A taxa de juros necessária é {i:.2f}% a.m!!')
