# 💼 Contabilidade Inteligente com IA 🤖

Este projeto demonstra como a Inteligência Artificial pode ser aplicada no contexto de contabilidade para automatizar tarefas, responder perguntas sobre dados contábeis e oferecer insights em tempo real. A versão atual reduz até 15% do tempo gasto com procuras e respostas de perguntas graças a um chatbox que lê e funciona como um chatGPT e responde suas perguntas e trás soluções. 

---

## ✅ Objetivo

Criar um sistema simples e funcional que:
- Utilize **dados contábeis públicos** (ou simulados).
- Permita **consultas inteligentes via IA**.
- Rode de forma gratuita no **Google Colab**.
- Possua uma interface simples com **chatbox interativo** (usando Streamlit ou similar).
- Seja uma base para versões futuras com mais funcionalidades.

---

## 🚀 Versão 1.0 — MVP (Produto Mínimo Viável)

Nesta versão, implementamos:

✅ **Banco de dados público simulado** com dados de despesas, receitas e impostos  
✅ **Código em Python (100% gratuito)** executável no Google Colab  
✅ **Chatbot inteligente** baseado em GPT (via API ou local com fallback)  
✅ Capacidade de fazer perguntas como:
> “Quais foram as despesas da empresa X em fevereiro?”  
> “Qual foi o imposto total em 2022?”

---

## 🔍 Etapas da Versão 1.0

1. **Download do Dataset Público**
   - Dataset: [Brazilian Stock Market - Kaggle](https://www.kaggle.com/datasets/therasforfinance/brazilian-stock-market-price-and-fundamentals)

2. **Exploração dos Dados**
   - Leitura com `pandas`
   - Limpeza e tratamento inicial

3. **Desenvolvimento de IA**
   - Aplicação de `Langchain` ou `pandas-ai` para consultas em linguagem natural
   - Exemplo: *"Qual foi o lucro líquido da empresa XYZ em 2021?"*

4. **Protótipo de Chatbot**
   - Interface simples via terminal ou Jupyter
   - Integração com IA para responder perguntas sobre os dados

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Google Colab
- Pandas
- OpenAI API (opcional)
- Streamlit (futuramente)
- SQLite / CSV como banco de dados
- HuggingFace / LangChain (futuramente)

---

## 🧠 Banco de Dados

Usaremos um conjunto de dados públicos/simulados com as seguintes colunas:

| Empresa | Data       | Tipo       | Valor    |
|---------|------------|------------|----------|
| Empresa X | 2023-02-15 | Imposto    | 2500.00  |
| Empresa Y | 2023-02-17 | Receita    | 12000.00 |
| Empresa Z | 2023-03-01 | Despesa    | 1500.00  |

Fonte: [base simulada](#) (iremos definir ou criar)

---

## ▶️ Como executar

1. Acesse o [Google Colab Notebook](#) (link será adicionado)
2. Suba o arquivo CSV ou use o arquivo pré-carregado
3. Insira sua OpenAI API Key (opcional – o código funciona com respostas locais simples também)
4. Faça perguntas no campo de input
5. Veja as respostas geradas pela IA com base no banco de dados

---

## 💡 Exemplos de perguntas que o sistema entende

- “Quanto a empresa X gastou com impostos em 2024?”
- “Quais empresas tiveram receita em março?”
- “Qual o total de despesas entre janeiro e abril?”

---

## 📈 Próximas versões

| Versão | Funcionalidade |
|--------|----------------|
| 1.1    | Interface visual com Streamlit |
| 1.2    | Integração com banco de dados real (SQLite ou PostgreSQL) |
| 2.0    | Classificação automática de documentos com ML |
| 2.1    | Análise preditiva de fluxo de caixa |
| 3.0    | Integração com sistemas de contabilidade reais via API |

---

## 📂 Estrutura do Projeto

📁 ia-contabilidade │ 

├── data/ 

│ └── contabilidade_simulada.csv 

│ ├── chatbot_colab.ipynb 

├── README.md 

└── requirements.txt 

---

## 👨‍💻 Autor

Este projeto está sendo desenvolvido por Leonardo Santos Medeiros, como parte de seu portfólio de **IA aplicada à Contabilidade**.  
Contribuições, dúvidas e sugestões são bem-vindas!
