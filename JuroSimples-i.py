""" Este programa irá encontrar a taxa de juros ao MÊS necessários para uma aplicação em juros simples """

pv = float(input(f'Digite o valor da aplicação: R$ '))
fv = float(input(f'Digite o valor que deseja acumular: R$ '))
n = float(input(f'Digite o número de meses da aplicação: '))
i = (fv/pv - 1) / n * 100

print(f'A taxa de juros é {i:.2f}% ao mês para obter montante final.')
