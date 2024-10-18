""" Esse programa irá dar o montante final com base em duas aplicações iniciais """

n = int(input('Digite o tempo das aplicações em nº de meses: '))
pv1 = float(input(f'Digite o valor da 1º aplicação: R$ '))
i1 = float(input(f'Digite a taxa a.a da 1º aplicação: '))
pv2 = float(input(f'Digite o valor da 2º aplicação: R$ '))
i2 = float(input(f'Digite a taxa a.m da 2º aplicação: '))

fv1 = pv1 * (1 + (i1/100)) ** (n/12)
fv2 = pv2 * (1 + (i2/100)) ** n
montante = fv1 + fv2

print(f'O valor final do montante é {montante:.2f}')
