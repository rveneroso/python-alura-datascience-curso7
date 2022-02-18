import pandas as pd
import funcoes_graficos as fg
import matplotlib.pyplot as plt

chocolura = pd.read_csv('../data/chocolura.csv')
# Converte a coluna mes para datetime
chocolura['mes'] = pd.to_datetime(chocolura['mes'])

chocolura['aumento'] = chocolura['vendas'].diff()
chocolura['aceleracao'] = chocolura['aumento'].diff()

chocolura.to_csv('../data/chocolura_convertido.csv', index=False)

fg.plotar(chocolura,'Vendas Chocolura no período de 2017 a 2018','Meses',
          'Vendas (R$)','mes','vendas')
plt.show()
fg.plotar(chocolura,'Aumento no número de vendas Chocolura entre 2017 e 2018','Meses',
          'Aumento das vendas','mes','aumento')
plt.show()
fg.plotar(chocolura,'Aceleração do aumento das vendas Chocolura entre 2017 e 2018','Meses',
          'Aceleração nas vendas','mes','aceleracao')
plt.show()