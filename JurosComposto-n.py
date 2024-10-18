""" Essa programa irá encontrar o tempo em dias corridos de um investimento """

import math

pv = float(input(f'Digite valor inicial do investimento: R$ '))
fv = float(input(f'Digite o valor final que deseja acumular: R$ '))
i = float(input(f'Digite o juros a.a em porcentagem: ')) / 100
ln1 = math.log(fv / pv)
ln2 = math.log(1 + i)
n = (ln1 / ln2) * 360

print(f'Você precisará de {n:.0f} dias corridos para atingir o montante final!')
