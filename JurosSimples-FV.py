""" Este programa irá encontrar o FUTURE VALUE para uma aplicação em juros simples """

pv = float(input(f'Digite o valor da aplicação: R$ '))
n = float(input(f'Digite o número de meses da aplicação: '))
i = float(input(f'Digite a taxa de juros ao mês em porcentagem: ')) / 100

fv = pv * (1 + i * n)
print(f'O valor do montante final é R$ {fv:.2f}!')
