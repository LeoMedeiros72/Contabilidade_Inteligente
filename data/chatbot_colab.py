# Instalação das bibliotecas necessárias
!pip install pandas sqlalchemy psycopg2 pyarrow openai==0.28

# Importações
import zipfile
import os
import shutil
import pandas as pd
from sqlalchemy import create_engine, text
from google.colab import drive

# Montar o drive
drive.mount('/content/drive')


# -------------------- EXTRAÇÃO DE ARQUIVOS ZIP --------------------

# Caminho completo para o arquivo ZIP
caminho_zip = '/content/drive/MyDrive/ProjetoIA_ML/archive.zip'

# Caminho para a pasta onde os arquivos serão extraídos
pasta_extraida = '/content/drive/MyDrive/ProjetoIA_ML/extracted/'

# Verificar se o arquivo ZIP existe
if os.path.exists(caminho_zip):
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_extraida)
    print("Arquivo extraído com sucesso!")
else:
    print("Arquivo ZIP não encontrado. Verifique o caminho.")

# -------------------- LEITURA DE ARQUIVOS CSV --------------------

# Vamos tentar carregar qualquer arquivo CSV encontrado na pasta extraída
for arquivo in os.listdir(pasta_extraida):
    if arquivo.endswith('.csv'):
        caminho_csv = os.path.join(pasta_extraida, arquivo)
        df_csv = pd.read_csv(caminho_csv)
        print(f"Exibindo as primeiras linhas do arquivo CSV: {arquivo}")
        print(df_csv.head())  # Exibe as 5 primeiras linhas para inspecionar

# -------------------- LEITURA DE ARQUIVOS PARQUET --------------------

# Função para percorrer pastas e carregar arquivos Parquet
for root, dirs, files in os.walk(pasta_extraida):
    print(f"Verificando a pasta: {root}")  # Imprime o diretório atual
    for arquivo in files:
        print(f"Encontrado arquivo: {arquivo}")  # Imprime o nome do arquivo
        if arquivo.endswith('.parquet'):
            caminho_parquet = os.path.join(root, arquivo)
            print(f"Lendo arquivo Parquet: {caminho_parquet}")  # Exibe o caminho do arquivo
            df_parquet = pd.read_parquet(caminho_parquet)
            print(f"Exibindo as primeiras linhas do arquivo Parquet: {arquivo}")
            print(df_parquet.head())  # Exibe as 5 primeiras linhas para inspecionar

# -------------------- CONEXÃO E CRIAÇÃO DO BANCO DE DADOS --------------------

# Criação da conexão com o banco SQLite
engine = create_engine('sqlite:///seu_banco.db')

# Instruções SQL para criar as tabelas
create_tables = [
    """
    CREATE TABLE IF NOT EXISTS empresas (
        cnpj TEXT PRIMARY KEY,
        nome_razao_social TEXT,
        setor TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS indicadores_financeiros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT,
        data DATE,
        receita_bruta REAL,
        lucro_bruto REAL,
        lucro_liquido REAL,
        ebitda REAL,
        outros_indicadores TEXT,
        FOREIGN KEY (cnpj) REFERENCES empresas(cnpj)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS dividendos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT,
        data_pagamento DATE,
        valor REAL,
        FOREIGN KEY (cnpj) REFERENCES empresas(cnpj)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS precos_acoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT,
        data DATE,
        preco_acao REAL,
        FOREIGN KEY (cnpj) REFERENCES empresas(cnpj)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS lancamentos_contabeis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT,
        tipo_lancamento TEXT,
        descricao TEXT,
        valor REAL,
        data DATE,
        FOREIGN KEY (cnpj) REFERENCES empresas(cnpj)
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS relacionamento_cvm (
        cnpj TEXT PRIMARY KEY,
        cod_cvm TEXT,
        nome_empresa TEXT,
        data_registro DATE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS lancamento_conta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT,
        cod_lancamento_conta TEXT,
        nome_lancamento_conta TEXT,
        valor REAL,
        data DATE,
        FOREIGN KEY (cnpj) REFERENCES empresas(cnpj)
    );
    """
]

# Executa cada comando SQL para criar as tabelas
with engine.connect() as connection:
    for statement in create_tables:
        connection.execute(text(statement))

# -------------------- VERIFICAÇÃO DE TABELAS --------------------

# Conectando ao banco e verificando as tabelas existentes
with engine.connect() as connection:
    result = connection.execute(text("PRAGMA table_list;"))
    tables = result.fetchall()
    print("Tabelas no banco de dados:")
    for table in tables:
        print(table[1])  # Exibe o nome de cada tabela

# -------------------- BACKUP DO BANCO DE DADOS --------------------

# Caminho para o banco de dados e para o backup
db_path = 'seu_banco.db'
backup_path = 'meu_banco_backup.db'

# Fazer o backup do banco de dados
shutil.copy(db_path, backup_path)
print("Backup realizado com sucesso para:", backup_path)

# -------------------- OBTER CAMINHO ABSOLUTO DO BANCO --------------------

# Definindo o nome do banco de dados
banco_nome = 'seu_banco.db'

# Obter o caminho absoluto do banco de dados
caminho_absoluto = os.path.abspath(banco_nome)
print("Caminho absoluto do banco:", caminho_absoluto)

# -------------------- CONEXÃO AO BANCO COM CAMINHO ABSOLUTO --------------------

# Caminho absoluto do banco de dados
caminho_banco = '/content/seu_banco.db'

# Conectando ao banco de dados SQLite com SQLAlchemy
engine = create_engine(f"sqlite:///{caminho_banco}")

# Verificando as tabelas para ter certeza da conexão
with engine.connect() as connection:
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    tables = result.fetchall()
    print("Tabelas no banco de dados:")
    for table in tables:
        print(table[0])  # Exibe o nome de cada tabela



import pandas as pd
import os
import zipfile
from sqlalchemy import create_engine

# -------------------- CRIAR DATAFRAME PARA CADA TABELA CSV OU PARQUET --------------------

# Caminhos
caminho_zip = '/content/drive/MyDrive/ProjetoIA_ML/archive.zip'
pasta_extraida = '/content/drive/MyDrive/ProjetoIA_ML/extracted/'

# Conexão com o banco SQLite (pode ser outro, como PostgreSQL etc.)
engine = create_engine('sqlite:///meu_banco_contabilidade.db')

# Extrair os arquivos ZIP
if os.path.exists(caminho_zip):
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_extraida)
    print("ZIP extraído com sucesso!")

# -------------------- EXIBIR DATAFRAMES QUE DERAM CERTO QTD DE LINHAS E LOG ERRADOS  --------------------

# Iterar sobre arquivos extraídos
for root, dirs, files in os.walk(pasta_extraida):
    for arquivo in files:
        caminho_completo = os.path.join(root, arquivo)
        nome_base = os.path.splitext(arquivo)[0].lower().replace('-', '_').replace(' ', '_')
        
        try:
            if arquivo.endswith('.csv'):
                df = pd.read_csv(caminho_completo)
            elif arquivo.endswith('.parquet'):
                df = pd.read_parquet(caminho_completo)
            else:
                continue  # Ignora outros arquivos

            df.to_sql(nome_base, engine, if_exists='replace', index=False)
            print(f"✅ Tabela '{nome_base}' criada com sucesso com {len(df)} linhas.")
        
        except Exception as e:
            print(f"❌ Erro ao processar {arquivo}: {e}")


# -------------------- EXIBIR DATAFRAMES PARA ANÁLISE  --------------------


from sqlalchemy import inspect

insp = inspect(engine)
tabelas = insp.get_table_names()
print("Tabelas disponíveis:", tabelas)

# Exibir as primeiras linhas de cada tabela
for tabela in tabelas:
    df = pd.read_sql_table(tabela, engine)
    display(f"\n📄 Tabela: {tabela}")
    display(df.head())
