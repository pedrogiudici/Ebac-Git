import pandas as pd
import seaborn as sns

gas_pd = pd.read_csv('/content/Ebac-Git/gasolina.csv')
grafico = sns.lineplot(data=gas_pd, x='dia', y='venda', palette='dark')
grafico.set(title='Preço médio da gasolina', xlabel='Dia', ylabel='Preço (R$)')
grafico.figure.savefig('gasolina.png')