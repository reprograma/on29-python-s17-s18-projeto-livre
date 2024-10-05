import pandas as pd
import os

diretorio_csv = os.path.abspath("source/bases")
arquivos_csv = [f"ESTACAO_{i}.csv" for i in range(1, 593)]

def read_csv(caminho_arquivo):
    df = pd.read_csv(caminho_arquivo, delimiter=';', skiprows=10)
    df.fillna(method='ffill', inplace=True)
    df['Data Medicao'] = pd.to_datetime(df['Data Medicao'], errors='coerce')
    df['PRECIPITACAO TOTAL, MENSAL (AUT)(mm)'] = df['PRECIPITACAO TOTAL, MENSAL (AUT)(mm)'].str.replace(',', '.').astype(float)
    df['PRESSAO ATMOSFERICA, MEDIA MENSAL (AUT)(mB)'] = df['PRESSAO ATMOSFERICA, MEDIA MENSAL (AUT)(mB)'].str.replace(',', '.').astype(float)
    df['TEMPERATURA MEDIA, MENSAL (AUT)(°C)'] = df['TEMPERATURA MEDIA, MENSAL (AUT)(°C)'].str.replace(',', '.').astype(float)
    df['VENTO, VELOCIDADE MAXIMA MENSAL (AUT)(m/s)'] = df['VENTO, VELOCIDADE MAXIMA MENSAL (AUT)(m/s)'].str.replace(',', '.').astype(float)
    df['VENTO, VELOCIDADE MEDIA MENSAL (AUT)(m/s)'] = df['VENTO, VELOCIDADE MEDIA MENSAL (AUT)(m/s)'].str.replace(',', '.').astype(float)
    return df

dataframes = []

for arquivo in arquivos_csv:
    caminho_arquivo = os.path.join(diretorio_csv, arquivo)
    try:
        df = read_csv(caminho_arquivo)
        dataframes.append(df)
    except Exception as e:
        print(f"Erro ao ler o arquivo {arquivo}: {e}")

if dataframes:
    df_combinado = pd.concat(dataframes, ignore_index=True)
    df_combinado.columns = df_combinado.columns.str.replace('[^A-Za-z0-9_]+', '_', regex=True)
    df_combinado.to_csv("source/dataset_com_todos_csvs.csv", index=False)
else:
    print("Nenhum arquivo foi lido.")

