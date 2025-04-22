# 💼 Contabilidade Inteligente com IA 🤖

Este projeto demonstra como a Inteligência Artificial pode ser aplicada no contexto de contabilidade para automatizar tarefas, responder perguntas sobre dados contábeis e oferecer insights em tempo real. A versão atual reduz até 15% do tempo gasto com procuras e respostas de perguntas, usando uma base de dados e algoritmos de IA. O chatbox, que vai permitir interações mais naturais, será implementado em versões futuras.

---

## ✅ Objetivo

Criar um sistema simples e funcional que:
- Utilize **dados contábeis públicos** (ou simulados).
- Permita **consultas inteligentes via IA**.
- Rode de forma gratuita no **Google Colab**.
- Possua uma interface simples com **chatbox interativo** (a ser implementado em versões futuras).
- Seja uma base para versões futuras com mais funcionalidades.

---

## 🚀 Versão 1.0 — MVP (Produto Mínimo Viável)

Nesta versão, implementamos:

✅ **Banco de dados público simulado** com dados de despesas, receitas e impostos  
✅ **Código em Python (100% gratuito)** executável no Google Colab  
✅ **Base de dados SQLite** armazenada no Google Drive (ainda não há chatbox interativo nesta versão)  
✅ **Capacidade de fazer perguntas sobre os dados contábeis** (sem chatbox interativo para agora, mas estará disponível futuramente)

**Exemplos de perguntas**:
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

4. **Banco de Dados SQLite**
   - Dados armazenados em um banco de dados SQLite no Google Drive, acessível por Python
   - A base de dados contém tabelas como `empresas`, `indicadores_financeiros`, `dividendos`, `precos_acoes`, entre outras.

   **Exemplo de Dados:**

   | Empresa    | Data       | Tipo     | Valor   |
   |------------|------------|----------|---------|
   | Petrobras  | 2022-06-30 | Receita  | 15000.00|
   | Vale S.A.  | 2022-06-30 | Imposto  | 2000.00 |
   | Ambev      | 2022-07-01 | Despesa  | 5000.00 |

   Esses dados são retirados do conjunto de dados [Brazilian Stock Market - Kaggle](https://www.kaggle.com/datasets/therasforfinance/brazilian-stock-market-price-and-fundamentals).

5. **Protótipo de Chatbot**
   - **Chatbox interativo** será implementado em versões futuras utilizando `Streamlit`
   - Por enquanto, o código oferece respostas simples via IA, mas sem interface de chat.

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- Google Colab
- Pandas
- OpenAI API (opcional)
- Streamlit (futuramente)
- SQLite (banco de dados)
- HuggingFace / LangChain (futuramente)

---

## 🧠 Banco de Dados

Usaremos um conjunto de dados públicos/simulados com as seguintes colunas, armazenadas em um banco de dados SQLite no Google Drive:

| Empresa    | Data       | Tipo     | Valor   |
|------------|------------|----------|---------|
| Petrobras  | 2022-06-30 | Receita  | 15000.00|
| Vale S.A.  | 2022-06-30 | Imposto  | 2000.00 |
| Ambev      | 2022-07-01 | Despesa  | 5000.00 |

O banco de dados contém as seguintes tabelas:

- **empresas**: informações sobre as empresas.
- **indicadores_financeiros**: dados financeiros como receita bruta, lucro líquido, etc.
- **dividendos**: informações sobre dividendos pagos.
- **precos_acoes**: preços das ações das empresas.

Fonte: [base simulada - Kaggle](https://www.kaggle.com/datasets/therasforfinance/brazilian-stock-market-price-and-fundamentals)

---

## 📂 Google Drive - Banco de Dados

Os arquivos de dados são armazenados em uma pasta pública no Google Drive, que pode ser acessada para leitura. Aqui está o link para a pasta pública:

[Google Drive - Pasta Pública com Dados Contábeis](https://drive.google.com/drive/folders/1uCtLvsC2uwcyNNXxTPpLJTeNib20c_fV?usp=sharing)

---

## ▶️ Como executar

1. Acesse o [Google Colab Notebook](https://colab.research.google.com/drive/1LWPcXVSdN8A_4_E_Yzc7B0gHO-j5kEHQ?usp=sharing)
2. Suba o arquivo CSV ou use o arquivo pré-carregado
3. Insira sua OpenAI API Key (opcional – o código funciona com respostas locais simples também)
4. Conecte-se ao banco de dados SQLite (salvo no Google Drive)
5. Faça perguntas no campo de input
6. Veja as respostas geradas pela IA com base no banco de dados

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

│ ├── chatbot_colab.py

├── README.md 

└── requirements.txt 

---

## 👨‍💻 Autor

Este projeto está sendo desenvolvido por Leonardo Santos Medeiros, como parte de seu portfólio de **IA aplicada à Contabilidade**.  
Contribuições, dúvidas e sugestões são bem-vindas!

O nome do repositório é **Contabilidade_Inteligente** e o arquivo Python está dentro da pasta `data/` como `chatbot_colab.py`.  
Se você deseja contribuir ou fazer sugestões, por favor, crie uma **issue** ou envie um **pull request**!

---

## 🤝 Contribuindo

Sinta-se à vontade para contribuir para o projeto! Para isso, basta seguir os seguintes passos:

1. Faça um **fork** deste repositório.
2. Crie uma **branch** com uma nova funcionalidade ou correção.
3. Faça o **commit** das suas alterações.
4. Envie um **pull request** com uma descrição clara do que foi alterado e por que.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
