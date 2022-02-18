import pandas as pd
import matplotlib.pyplot as plt
import funcoes_graficos as fg

alucar = pd.read_csv('../data/alucar_convertido.csv')

# Gera um gráfico com baseado no aumento de vendas ao longo dos meses. Esse gráfico será idêntico ao gráfico
# de vendas criado no script alucar_analisando_vendas.py.

# Gráfico com o aumento das vendas entre 2017 e 2018
fg.plotar(alucar,'Aumento nas Vendas da Alucar entre 2017 e 2018','Meses',
          'Vendas (R$)','mes','aumento')

# Gráfico com a aceleração no aumento das vendas entre 2017 e 2018
fg.plotar(alucar,'Aceleração do aumento nas Vendas da Alucar entre 2017 e 2018','Meses',
          'Aumento de Vendas (R$)','mes','aceleracao')
plt.show()