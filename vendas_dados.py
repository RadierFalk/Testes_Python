import pandas as pd
from IPython.display import display

#Funcionamento
#Forma mais básica (muitas vezes não usaremos a forma mais básica)
#dataframe = pd.read_csv(arquivo existente)

vendas_df = pd.read_csv("dados/Contoso - Vendas  - 2017.csv", sep=';')
produtos_df = pd.read_csv("dados/Contoso - Cadastro Produtos.csv", sep=';')
lojas_df = pd.read_csv("dados/Contoso - Lojas.csv", sep=';')
clientes_df = pd.read_csv("dados/Contoso - Clientes.csv", sep=';')

#display(vendas_df)
#display(produtos_df)
#display(lojas_df)
#display(clientes_df)

#-----Metodo para tirar colunar da exibição-------

#clientes_df = clientes_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10'], axis=1)
#display(clientes_df)

clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['Nome da Marca', 'ID Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]


#display(clientes_df)
#display(produtos_df)



#vendas_df[['Numero da Venda', 'Data da Venda', 'ID Produto']]

#vendas_df.info()

#lista_de_clientes = vendas_df['ID Cliente']

#lista_colunas = ['ID Produto', 'Quantidade Vendida', 'Quantidade Devolvida']
#produtos_quant = vendas_df[lista_colunas]

#print(produtos_quant)


#Juntando os Dataframes

vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

#Exibindo dataframe mesclados

#display(vendas_df)

#renomeano colunas

vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do Cliente'})
#display(vendas_df)

#Qual cliente comprou mais vezes? Metodo:

freq_clientes = vendas_df['E-mail do Cliente'].value_counts()
#display(freq_clientes)
freq_clientes[:5].plot(title='Frequencia Clientes')