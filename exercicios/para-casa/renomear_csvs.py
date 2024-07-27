import os

pasta_csv =  os.path.abspath("source/bases")

todos_arquivos = os.listdir(pasta_csv)
arquivos_csv = [f for f in todos_arquivos if f.endswith('.csv')]
arquivos_csv.sort()

for index, arquivo in enumerate(arquivos_csv, start=1):
    novo_nome = f"ESTACAO_{index}.csv"
    original = os.path.join(pasta_csv, arquivo)
    novo_arquivo = os.path.join(pasta_csv, novo_nome)
    os.rename(original, novo_arquivo)
    print(f"{arquivo} -> {novo_nome}")

print("Renomeação concluída.")
