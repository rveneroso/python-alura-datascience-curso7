import pandas as pd
import funcoes_graficos as fg
import matplotlib.pyplot as plt

alucel = pd.read_csv('../data/alucel.csv')
# Converte a coluna dia para datetime
alucel['dia'] = pd.to_datetime(alucel['dia'])

alucel['aumento'] = alucel['vendas'].diff()
alucel['aceleracao'] = alucel['aumento'].diff()

# Calcula a média móvel das vendas da Alucel com base em um período de 7 dias.
alucel['media_movel'] = alucel['vendas'].rolling(7).mean()
alucel['media_movel_21'] = alucel['vendas'].rolling(21).mean()

alucel.to_csv('../data/alucel_convertido.csv', index=False)

fg.plotar(alucel, 'Análise de vendas com média móvel de 7 dias', 'Tempo', 'Média Móvel', 'dia', 'media_movel' )
fg.plotar(alucel, 'Análise de vendas com média móvel de 21 dias', 'Tempo', 'Média Móvel', 'dia', 'media_movel_21' )
plt.show()
# fg.plotar(alucel,'Vendas alucel no período de 2017 a 2018','dias',
#           'Vendas (R$)','dia','vendas')
#
# fg.plotar(alucel,'Aumento no número de vendas alucel entre 2017 e 2018','dias',
#           'Aumento das vendas','dia','aumento')
# plt.show()
# fg.plotar(alucel,'Aceleração do aumento das vendas alucel entre 2017 e 2018','dias',
#           'Aceleração nas vendas','dia','aceleracao')
# plt.show()