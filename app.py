import pandas as pd
import streamlit as st
import plotly.express as px

# Caminho do arquivo de origem (com abas "Pagamentos", "Transferencias", "Recebimentos")
source_file_path = "Fluxo de caixa.xlsx"

# Caminho do arquivo de destino (Data Lake)
target_file_path = "Datalake.xlsx"

# Etapa 1: Leitura das tabelas e consolidação
pagamentos = pd.read_excel(source_file_path, sheet_name="Pagamentos")
pagamentos["Origem"] = "Pagamento"

transferencias = pd.read_excel(source_file_path, sheet_name="Transferencias")
transferencias["Origem"] = "Transferência"

recebimentos = pd.read_excel(source_file_path, sheet_name="Recebimentos")
recebimentos["Origem"] = "Recebimento"

# Concatenar as tabelas
tabela_combinada = pd.concat([pagamentos, transferencias, recebimentos], ignore_index=True)

# Tratar os dados
tabela_combinada['Data'] = pd.to_datetime(tabela_combinada['Data'], errors='coerce')
tabela_combinada['Mes'] = tabela_combinada['Data'].dt.to_period('M')  # Adicionar coluna de mês
tabela_combinada.fillna(0, inplace=True)

# Salvar a tabela consolidada no arquivo de destino
with pd.ExcelWriter(target_file_path, engine="openpyxl") as writer:
    tabela_combinada.to_excel(writer, sheet_name="Consolidado", index=False)

print(f"Tabelas consolidadas com sucesso no arquivo: {target_file_path}")

# Dashboards

# Carregando dados
df = pd.read_excel("Datalake.xlsx")
print(df)
# Transformando coluna data em data
df["Data"] = pd.to_datetime(df["Data"])

# Organizando dados
df = df.sort_values("Data")

# Selecionando os meses
df["Mês"] = df["Data"].apply(lambda x: str(x.year) + "-" + str(x.month))
print("mes completo")
# Filtro mês
month = st.sidebar.selectbox("Mês", df["Mês"].unique())

streamlit run c:/Users/Lenovo/Downloads/Projeto join 1.0/app.py

