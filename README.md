# 📊 Inteligência Competitiva no Varejo de Smartphones

Projeto completo de análise e visualização de dados com foco em **Inteligência Competitiva**, integrando **Big Data**, **Web Scraping**, **Análise Exploratória**, **Previsão de Preços**, **Tendências de Busca** e **Reputação de Marcas** no segmento de **smartphones**.

---

## 📌 Objetivo

Desenvolver uma solução de Inteligência Competitiva no varejo eletrônico (com foco inicial em smartphones), utilizando técnicas de ciência de dados para:

- Analisar preços e tendências do mercado
- Prever variações de preços
- Avaliar a reputação das marcas (Reclame Aqui)
- Medir popularidade via Google Trends
- Apresentar insights em um **dashboard interativo com Streamlit**

---

##  Tecnologias Utilizadas

- **Python 3.11+**
- **Pandas / Numpy**
- **Matplotlib / Seaborn**
- **Scikit-learn**
- **Prophet (Facebook)**
- **selenium(scraping da Amazon)
- **BeautifulSoup** (Reclame Aqui)
- **PyTrends** (Google Trends)
- **Streamlit** (dashboard)
- **SQLite / CSVs** (armazenamento)

---

## 🏗️ Estrutura do Projeto

rojeto-inteligencia-competitiva/ 
├── data/ │ ├── raw/ # Dados brutos coletados │ ├── processed/ # Dados tratados ├── notebooks/ │ ├── 01_analise_exploratoria.ipynb │ └── 02_previsao_precos.ipynb ├── scrapers/ │ ├── amazon_scraper/ # Scrapy + Playwright │ └── reclame_aqui.py # BeautifulSoup ├── app/ │ └── streamlit_app.py # Dashboard interativo ├── requirements.txt └── README.md