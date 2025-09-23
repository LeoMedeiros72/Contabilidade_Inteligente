# Contabilidade Inteligente com IA

Este projeto demonstra como a Inteligência Artificial pode ser aplicada no contexto de contabilidade para automatizar tarefas, responder perguntas sobre dados contábeis e oferecer insights em tempo real.

Na versão atual, o sistema utiliza PostgreSQL como banco de dados e Flowise (com modelos de IA) para interpretar perguntas em português e convertê-las em consultas SQL automaticamente. Isso reduz até 15% do tempo gasto em consultas manuais de dados contábeis.

---

## ✅ Objetivo

Criar um sistema funcional que:
- Utilize **dados contábeis públicos** (ou simulados, a partir de datasets do Kaggle).  
- Permita **consultas inteligentes via IA em linguagem natural**.  
- Rode em ambiente **Docker**, garantindo portabilidade.  
- Tenha uma **interface interativa** com chatbox (em construção).  
- Sirva de base para futuras versões com mais funcionalidades.

---

## 🚀 Versão 1.1 — MVP com PostgreSQL + Flowise

Nesta versão, implementamos:

✅ **Banco de dados PostgreSQL** populado a partir de datasets públicos (Kaggle)  
✅ **Migração automática dos dados** usando Python (Pandas + SQLAlchemy)  
✅ **Integração com Flowise** para consultas em linguagem natural  
✅ **Configuração via Docker Compose** (Postgres + Flowise rodando em containers)  
✅ **Capacidade de responder a perguntas contábeis diretamente a partir do banco de dados**  

**Exemplos de perguntas no chat**:
> “Quais empresas distribuíram dividendos em 2023?”  
> “Qual foi a receita líquida da Petrobras em 2022?”  
> “Há contas vencendo hoje?”  

---

## 🔍 Etapas da Versão 1.1

1. **Download do Dataset Público**  
   - Dataset base: [Brazilian Stock Market - Kaggle](https://www.kaggle.com/datasets/therasforfinance/brazilian-stock-market-price-and-fundamentals)  

2. **Carregamento dos Dados**  
   - Extração automática de `.csv` e `.parquet` do arquivo `archive.zip`.  
   - Criação das tabelas principais no **Postgres**:  
     - `empresas`  
     - `indicadores_financeiros`  
     - `dividendos`  
     - `precos_acoes`  
     - `lancamentos_contabeis`  
     - `lancamento_conta`  
     - `relacionamento_cvm`  

3. **Configuração do Banco**  
   - Banco Postgres rodando em container Docker.  
   - Dados carregados diretamente via script Python (`migrate.py`).  

4. **Integração com IA via Flowise**  
   - Uso de **Chain Tool** + **SQL Database Chain**.  
   - Modelo LLM (`Gemini 2.5 Flash`) traduz perguntas em SQL.  
   - Respostas sempre em **português do Brasil**, resumidas de forma clara.

---

## 🛠️ Tecnologias utilizadas

- **Python 3.12+**  
- **Docker + Docker Compose**  
- **PostgreSQL** (banco de dados)  
- **Flowise** (orquestração de LLM + SQL)  
- **Pandas + SQLAlchemy** (para migração de dados)  
- **LangChain** (base para o agente SQL)  
- **Streamlit** (futuro chatbox interativo)  

---

## 📂 Estrutura do Projeto

📁 contabilidade-inteligente │  
├── database/  
│   └── contabilidade.db *(backup inicial em SQLite)*  
├── docker-compose.yml *(orquestração Postgres + Flowise)*  
├── migrate.py *(script para migrar dados do ZIP → Postgres)*  
├── README.md  
└── requirements.txt  

---

## ▶️ Como executar

1. Clone o repositório  
   ```bash
   git clone https://github.com/seuusuario/Contabilidade_Inteligente.git
   cd Contabilidade_Inteligente```

2. Suba os containers com Docker Compose
   ```bash
   docker compose up -d```

3. Acesse o Flowise
   [http://localhost:3000](http://localhost:3000)

4. Conecte-se ao Postgress (ex. Via DBeaver)
```bash
Host: localhost
Port: 5432
Database: contabilidade
User: contab_user
Password: contab_pass
```

5. Faça perguntas no chat (Flowise)  
- “Quais empresas pagaram dividendos em 2022?”  
- “Qual o preço da ação PETR4 em março de 2023?”  

---

## 📈 Próximas versões

| Versão | Funcionalidade |
|--------|----------------|
| 1.2    | Interface visual com Streamlit integrada ao Postgres |
| 2.0    | Classificação automática de documentos contábeis com ML |
| 2.1    | Análise preditiva de fluxo de caixa |
| 3.0    | Integração com sistemas reais de contabilidade via API |

---

## 👨‍💻 Autor

Projeto desenvolvido por **Leonardo Santos Medeiros**, como parte do portfólio de **IA aplicada à Contabilidade**.  

Contribuições, dúvidas e sugestões são bem-vindas!  

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.  

