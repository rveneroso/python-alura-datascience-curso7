import pandas as pd
import funcoes_graficos as fg
import matplotlib.pyplot as plt

cafelura = pd.read_csv('../data/cafelura.csv')
# Converte a coluna mes para datetime
cafelura['mes'] = pd.to_datetime(cafelura['mes'])

# cafelura['aumento'] = cafelura['vendas'].diff()
# cafelura['aceleracao'] = cafelura['aumento'].diff()
cafelura.to_csv('../data/cafelura_convertido.csv', index=False)

cafelura = pd.read_csv('../data/cafelura_convertido.csv')

# A normalização das vendas consiste em dividir as vendas pelos números de fins de semana. Não sei porque é
# feito dessa forma.
# Retorna apenas a quantidade de dias dos fins de semana. O objeto retornado é <class 'numpy.ndarray'>
# Cada posição do array corresponde ao número de dias de fins de semana em cada mês.
qtd_dias_fins_semana = pd.read_csv('../data/dias_final_de_semana.csv')
# É um array bidimensional. Por isso precisamos pegar apenas apenas a primeira posição.
qtd_dias_fins_semana = qtd_dias_fins_semana['quantidade_de_dias'].values
print(cafelura['vendas'])
print(qtd_dias_fins_semana)
cafelura['vendas_normalizadas'] = cafelura['vendas'] / qtd_dias_fins_semana

fg.plotar(cafelura,'Vendas normalizadas da Cafelura de 2017 a 2018', 'Tempo', 'Vendas normalizadas', 'mes', 'vendas_normalizadas')
plt.show()