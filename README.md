# Projeto BI: Análise de Vendas com ETL em Python

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### 🔗 [Veja o Dashboard Interativo Aqui](https://link-para-seu-dashboard-aqui)

---

### 🎯 Conceito do Projeto

Este projeto demonstra uma abordagem de Business Intelligence focada na automação e flexibilidade do processo de ETL (Extração, Transformação e Carga) utilizando Python. O objetivo foi simular um cenário onde os dados chegam de fontes diversas (neste caso, múltiplos CSVs) e precisam ser limpos, transformados e consolidados programaticamente antes de serem carregados na ferramenta de BI.

---

### 🛠️ Arquitetura Utilizada

1.  **Fonte de Dados:** Dataset público de e-commerce da Olist, disponível no Kaggle.
2.  **Transformação (ETL):** Foi desenvolvido um script em **Python** (`tratar_dados.py`) utilizando a biblioteca **Pandas** para:
    * Carregar múltiplos arquivos CSV.
    * Juntar as informações em um único DataFrame (`merge`).
    * Limpar os dados (filtrar status de pedidos, tratar valores nulos).
    * Criar novas colunas para enriquecer a análise (feature engineering).
    * Exportar um único arquivo Excel (`.xlsx`) limpo e otimizado para análise.
3.  **Visualização:** O arquivo Excel gerado serviu como fonte de dados para o Power BI, onde as medidas DAX e os visuais foram criados para extrair insights.

Esta abordagem separa a camada de transformação (Python) da camada de apresentação (Power BI), facilitando a manutenção, a automação e a escalabilidade do fluxo de dados.

---

### 🚀 Como Reproduzir

1.  Clone este repositório.
2.  Crie uma pasta chamada `dados_brutos` e coloque os CSVs da Olist dentro dela.
3.  Instale as dependências listadas no `requirements.txt`: `pip install -r requirements.txt`.
4.  Execute o script Python para gerar o arquivo tratado: `python tratar_dados.py`.
5.  Abra o arquivo `.pbix` e, se necessário, atualize a fonte de dados para apontar para o arquivo Excel gerado na pasta `dados_tratados`.
