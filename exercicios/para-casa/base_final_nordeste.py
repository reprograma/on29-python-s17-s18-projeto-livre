import pandas as pd

df_estacoes_nordeste = pd.read_csv('estacoes_nordeste.csv')
df_base_final = pd.read_csv('base_final_tratada.csv')

codigos_estacao_nordeste = df_estacoes_nordeste['Estacao'].unique()
estados_nordeste = df_estacoes_nordeste['Sigla']
df_base_final_nordeste = df_base_final[df_base_final['Codigo_Estacao'].isin(codigos_estacao_nordeste)]

df_base_final_nordeste.to_csv('base_final_nordeste.csv', index=False)

print(df_base_final_nordeste.head())
