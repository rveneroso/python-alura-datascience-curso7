import pandas as pd
import funcoes_graficos as fg
import matplotlib.pyplot as plt

assinantes = pd.read_csv('../data/newsletter_alucar.csv')
# Converte a coluna mes para datetime
assinantes['mes'] = pd.to_datetime(assinantes['mes'])

assinantes['aumento'] = assinantes['assinantes'].diff()
assinantes['aceleracao'] = assinantes['aumento'].diff()

assinantes.to_csv('../data/newsletter_alucar_convertido.csv', index=False)

fg.plotar(assinantes,'Número de assinantes da Newsletter no Período de 2017 a 2018','Meses',
          'Número de Assinantes','mes','assinantes')
plt.show()
fg.plotar(assinantes,'Aumento no Número de Assinantes da Newsletter entre 2017 e 2018','Meses',
          'Número de Assinantes','mes','aumento')
plt.show()
fg.plotar(assinantes,'Aceleração do aumento do número de assinantes da Newsletter entre 2017 e 2018','Meses',
          'Aumento no número de assinantes','mes','aceleracao')
plt.show()