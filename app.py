import pandas as pd
from IPython.display import display
import plotly.express as px

# passo 1: Importar a base de dados

# passo 2: Tratamento da base de dados
#    - Excluir/corrigir linhas e colunas vazias
#    - Ajeitar colunas importadas
#    - Excluir colunas inúteis

# passo 3: Analisar a base de dados
#    - Queremos descobrir os principais motivos de cancelamento de cartão

##Passo 1: Importar a Base de Dados
tabela_clientes = pd.read_csv("ClientesBanco.csv", encoding="latin1")
tabela_clientes = tabela_clientes.drop("CLIENTNUM", axis=1) # excluindo coluna 
display(tabela_clientes)

##Passo 2: Tratamento da Base de Dados
tabela_clientes = tabela_clientes.dropna() # exclui as linhas que têm itens vazios
display(tabela_clientes.info())
display(tabela_clientes.describe())

##Passo 3: Analisar os Dados - Queremos descobrir o motivo do clientes cancelarem
display(tabela_clientes["Categoria"].value_counts())
display(tabela_clientes["Categoria"].value_counts(normalize=True))

""" Objetivo: Analisar o 80/20 - Regra de Pareto
Olhar todas as características dos clientas e descobrir os PRINCIPAIS MOTIVOS de cancelamento
"""

for coluna in tabela_clientes:
  # Passo 1 - criar a gráfico 
  fig = px.histogram(tabela_clientes, x=coluna, color="Categoria")
  # Passo 2 - exibir a gráfico
  fig.show()
  
  
"""Analisando os gráficos:

    1.   Quase todos os clientes que cancelaram são da categoria Blue
    2.   Quanto mais um cliente entra em contato o banco, maior a chance dele cancelar  
    - Plano de Ação: Analisar o motivo do contato/Tratar os clientes que mais entraram em contato com o banco 
    3.   Me parece que quem usa pouco o limite, cancela o cartão
     - Com mais de 80 transações o cliente não cancela mais o cartão
     - Clientes com menos de 60 transações são muito criticos
     - A mesma coisa acontece com a quantidade de transações
"""