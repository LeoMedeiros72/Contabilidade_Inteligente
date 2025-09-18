install pandas sqlalchemy psycopg2 pyarrow 
import os, zipfile, pandas as pd
from sqlalchemy import create_engine, text

# Conexão com Postgres (mesma rede do docker-compose)
engine_pg = create_engine("postgresql://admin:admin@postgres:5432/contabilidade")

# ---------------- EXTRAÇÃO ----------------
zip_path = "/app/archive.zip"
extract_path = "/app/extracted"
os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("✅ Arquivo extraído em:", extract_path)

# ---------------- CRIAR TABELAS ----------------
ddl_statements = [
    """
    CREATE TABLE IF NOT EXISTS empresas (
        cod_cnpj TEXT,
        nome_com_emp TEXT,
        desc_all_tickes TEXT,
        nome_ticker TEXT,
        data_inges TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS indicadores_financeiros (
        nome_infor TEXT,
        num_valor TEXT,
        desc_ticke_aberto TEXT,
        desc_ticke TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS dividendos (
        id_lancamento INT,
        desc_ticke_aberto TEXT,
        desc_ticke TEXT,
        desc_tipo_dividendos TEXT,
        num_valor_pago TEXT,
        data_ref TEXT,
        data_pagamento TEXT,
        num_qtd_acoes INT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS precos_acoes (
        id_lancamento INT,
        nome_ticker TEXT,
        nome_interv TEXT,
        data_cotacao TEXT,
        num_open TEXT,
        num_high TEXT,
        num_low TEXT,
        num_close TEXT,
        num_volume TEXT,
        anomes TEXT,
        fonte_periodo TEXT
    );
    """
]

with engine_pg.connect() as conn:
    for ddl in ddl_statements:
        conn.execute(text(ddl))
    print("✅ Estrutura criada no Postgres")

# ---------------- CARGA DOS DADOS ----------------

# EMPRESAS
csv_empresas = os.path.join(extract_path, "DE_PARA_CNPJ_CVM_MANUAL.csv")
if os.path.exists(csv_empresas):
    df_emp = pd.read_csv(csv_empresas)
    df_emp.to_sql("empresas", engine_pg, if_exists="append", index=False)
    print(f"✅ Empresas carregadas: {len(df_emp)}")

# INDICADORES
pasta_ind = os.path.join(extract_path, "FUNDAMENTUS_SOT_SCRAPING_INDICADORES")
if os.path.exists(pasta_ind):
    parquet_file = [f for f in os.listdir(pasta_ind) if f.endswith(".parquet")][0]
    df_ind = pd.read_parquet(os.path.join(pasta_ind, parquet_file))
    df_ind.to_sql("indicadores_financeiros", engine_pg, if_exists="append", index=False)
    print(f"✅ Indicadores carregados: {len(df_ind)}")

# DIVIDENDOS
pasta_div = os.path.join(extract_path, "FUNDAMENTUS_SOT_SCRAPING_DIVIDENDOS")
if os.path.exists(pasta_div):
    parquet_file = [f for f in os.listdir(pasta_div) if f.endswith(".parquet")][0]
    df_div = pd.read_parquet(os.path.join(pasta_div, parquet_file))
    df_div.to_sql("dividendos", engine_pg, if_exists="append", index=False)
    print(f"✅ Dividendos carregados: {len(df_div)}")

# PREÇOS
precos_paths = [
    "YAHOO_SOT_SCRAPING_PRICE_1D",
    "YAHOO_SOT_SCRAPING_PRICE_5D",
    "YAHOO_SOT_SCRAPING_PRICE_1WK",
    "YAHOO_SOT_SCRAPING_PRICE_1MO",
    "YAHOO_SOT_SCRAPING_PRICE_3MO"
]

for pasta in precos_paths:
    pasta_full = os.path.join(extract_path, pasta)
    if os.path.exists(pasta_full):
        parquet_file = [f for f in os.listdir(pasta_full) if f.endswith(".parquet")][0]
        df_preco = pd.read_parquet(os.path.join(pasta_full, parquet_file))
        df_preco["fonte_periodo"] = pasta
        df_preco.to_sql("precos_acoes", engine_pg, if_exists="append", index=False)
        print(f"✅ {pasta} carregado: {len(df_preco)}")

print("🎉 Migração concluída com sucesso!")
