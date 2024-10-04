import pandas as pd
#Funcionamento
#Forma mais básica (muitas vezes não usaremos a forma mais básica)
#dataframe = pd.read_csv(arquivo existente)

vendas_df = pd.read_csv("dados/Contoso - Cadastro Produtos.csv", sep=';')
print(vendas_df)