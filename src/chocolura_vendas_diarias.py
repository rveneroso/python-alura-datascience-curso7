import pandas as pd
import funcoes_graficos as fg
import matplotlib.pyplot as plt

dias_traduzidos = {'Monday': 'Segunda',
                   'Tuesday' : 'Terça',
                   'Wednesday':'Quarta',
                   'Thursday':'Quinta',
                   'Friday':'Sexta',
                   'Saturday':'Sábado',
                   'Sunday':'Domingo'}

vendas_por_dia = pd.read_csv('../data/vendas_por_dia.csv')

# Converte a coluna mes para datetime
vendas_por_dia['dia'] = pd.to_datetime(vendas_por_dia['dia'])

vendas_por_dia['aumento'] = vendas_por_dia['vendas'].diff()
vendas_por_dia['aceleracao'] = vendas_por_dia['aumento'].diff()

vendas_por_dia['dia_da_semana'] = vendas_por_dia ['dia'].dt.day_name()
# Traduz os nomes dos dias da semana
vendas_por_dia['dia_da_semana'] = vendas_por_dia['dia_da_semana'].map(dias_traduzidos)
# Agrupando os valores por dia e obtendo índices.
vendas_agrupadas = vendas_por_dia.groupby('dia_da_semana')['vendas', 'aumento', 'aceleracao'].mean().round()
print(vendas_agrupadas)
vendas_por_dia.to_csv('../data/chocolura_vendas_por_dia_convertido.csv', index=False)

fg.plotar(vendas_por_dia,'Vendas diárias em outubro e novembro','Dias',
          'Vendas (R$)','dia','vendas')
plt.show()
fg.plotar(vendas_por_dia,'Aumento no número de vendas diárias Chocolura em outubro e novembro','Dias',
          'Aumento das vendas','dia','aumento')
plt.show()
fg.plotar(vendas_por_dia,'Aceleração do aumento das vendas diárias Chocolura em outubro e novembro','Dias',
          'Aceleração nas vendas diárias em outubro e novembro','dia','aceleracao')
plt.show()