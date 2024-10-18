""" Este programa irá entrar o Present Value com base nas informações solicitadas """

fv = float(input(f'Digite valor de face da aplicação: R$ '))
n = int(input(f'Digite o prazo em dias úteis: '))
i = float(input(f'Digite a taxa em porcentagem a.a over: '))

pv = fv / (1 + (i/100)) ** (n/252)

print(f'O valor present da aplicação é {pv:.2f}!')
