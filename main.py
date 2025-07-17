"""Vamos realizar as leituras para registrar os dados, 
    criando assim um histórico no próprio banco de dados"""

#importando as bibliotecas
import pandas as pd
import mysql.connector

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='Cobrancas'
)
regis = conexao.cursor()

#Arquivo XLSX 
arqui = "C:/Users/henry/OneDrive/Documentos/Envio_" \
"mensagem/Envio_mensagem/Devedores.xlsx"

df_clientes = pd.read_excel(arqui, sheet_name="Perfil_Cliente")
df_titulos = pd.read_excel(arqui, sheet_name="Titulo_Vencido")

# INSERIR PERFIL_CLIENTE 
for idx, row in df_clientes.iterrows():
    sql = """
        INSERT INTO Perfil_Cliente (id_cliente, nome_empresa, cnpj, email, telefone)
        VALUES (%s, %s, %s, %s, %s)
    """
    regis.execute(sql, (
        idx + 1, 
        row['nome_empresa'], 
        row['cnpj'], 
        row['email'], 
        row['telefone']
    ))

# INSERIR TITULO_VENCIDO
for idx, row in df_titulos.iterrows():
    sql = """
        INSERT INTO Titulo_Vencido (id_titulo, cnpj, valor_contrato, data_pagamento, dias_atrasado, valor_juros)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    regis.execute(sql, (
        idx + 1, 
        row['cnpj'], 
        float(row['valor_contrato']), 
        pd.to_datetime(row['data_pagamento']).date(), 
        int(row['dias_atrasado']), 
        float(row['valor_juros'])
    ))


conexao.commit()
regis.close()
conexao.close()

print("Dados registrados")