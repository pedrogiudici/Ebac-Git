import pandas as pd
import seaborn as sns

gasolina_pd = pd.read_csv('gasolina.csv')
grafico = sns.lineplot(data=gasolina_pd, x='dia', y='venda', palette='pastel')
grafico.set(title='Preço médio da gasolina em São Paulo', xlabel='Dia', ylabel='Valor (R$)')
grafico.figure.savefig('gasolina.png')