import pandas as pd
import os

diretorio_csv = os.path.abspath("source/bases")
arquivos_csv = [f"ESTACAO_{i}.csv" for i in range(1, 593)]

def extrair_metadados(linhas):
    metadados = {}
    for linha in linhas[:9]: 
        chave, valor = linha.strip().split(": ", 1)
        metadados[chave] = valor
    return metadados

def ler_csv(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    metadados = extrair_metadados(linhas)

    dados = pd.read_csv(caminho_arquivo, delimiter=';', skiprows=9)
    dados.fillna(method='ffill', inplace=True)
    dados['Data Medicao'] = pd.to_datetime(dados['Data Medicao'], errors='coerce')
    dados['PRECIPITACAO TOTAL, MENSAL (AUT)(mm)'] = dados['PRECIPITACAO TOTAL, MENSAL (AUT)(mm)'].str.replace(',', '.').astype(float)
    dados['PRESSAO ATMOSFERICA, MEDIA MENSAL (AUT)(mB)'] = dados['PRESSAO ATMOSFERICA, MEDIA MENSAL (AUT)(mB)'].str.replace(',', '.').astype(float)
    dados['TEMPERATURA MEDIA, MENSAL (AUT)(°C)'] = dados['TEMPERATURA MEDIA, MENSAL (AUT)(°C)'].str.replace(',', '.').astype(float)
    dados['VENTO, VELOCIDADE MAXIMA MENSAL (AUT)(m/s)'] = dados['VENTO, VELOCIDADE MAXIMA MENSAL (AUT)(m/s)'].str.replace(',', '.').astype(float)
    dados['VENTO, VELOCIDADE MEDIA MENSAL (AUT)(m/s)'] = dados['VENTO, VELOCIDADE MEDIA MENSAL (AUT)(m/s)'].str.replace(',', '.').astype(float)

    for chave, valor in metadados.items():
        dados[chave] = valor

    return dados

dataframes = []

for arquivo in arquivos_csv:
    caminho_arquivo = os.path.join(diretorio_csv, arquivo)
    try:
        df = ler_csv(caminho_arquivo)
        dataframes.append(df)
    except Exception as e:
        print(f"Erro ao ler o arquivo {arquivo}: {e}")

if dataframes:
    df_combinado = pd.concat(dataframes, ignore_index=True)
    df_combinado.columns = df_combinado.columns.str.replace('[^A-Za-z0-9_]+', '_', regex=True)
    df_combinado.to_csv("source/base_final.csv", index=False)
else:
    print("Nenhum arquivo foi lido.")