""" Este programa irá encontrar o PRESENT VALUE para um valor final em juros simples """

fv = float(input(f'Digite o valor final do montante: R$ '))
n = float(input(f'Digite o número de meses da aplicação: '))
i = float(input(f'Digite a taxa de juros ao mês em porcentagem: ')) / 100

pv = fv / (1 + i * n)

print(f'O valor presente é R$ {pv:.2f}!')
