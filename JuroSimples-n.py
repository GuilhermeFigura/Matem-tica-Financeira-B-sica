""" Este programa irá encontrar o número de meses necessários de uma aplicação em juros simples """

pv = float(input(f'Digite o valor da aplicação: R$ '))
fv = float(input(f'Digite o valor que deseja acumular: R$ '))
i = float(input(f'Digite a taxa ao ano em %: ')) / 12
n = (fv/pv-1) / i * 100

print(f'Será necessário {n:.1f} meses para obter montante final.')
