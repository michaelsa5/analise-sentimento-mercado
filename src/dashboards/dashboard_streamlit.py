# src/dashboards/dashboard_streamlit.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv("data/processed/magalu_phones_clean.csv")
df['marcas'] = df['title'].str.extract(r'(^\w+)')

# Título
st.title("📱 Radar Varejo: Análise de Smartphones")

# Filtro de marca
marcas = df['marcas'].value_counts().index.tolist()
marca_selecionada = st.multiselect("Filtrar por Marca", marcas, default=marcas[:5])

df_filtrado = df[df['marcas'].isin(marca_selecionada)]

# Gráfico: distribuição de preços
st.subheader("Distribuição de Preços")
fig1, ax1 = plt.subplots()
sns.histplot(df_filtrado["price"], bins=20, kde=True, ax=ax1)
st.pyplot(fig1)

# Gráfico: preço médio por marca
st.subheader("Preço Médio por Marca")
df_group = df_filtrado.groupby("marcas")["price"].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
df_group.plot(kind='bar', color='green', ax=ax2)
ax2.set_ylabel("Preço Médio (R$)")
st.pyplot(fig2)

# Tabela de produtos
st.subheader("📋 Tabela de Produtos")
st.dataframe(df_filtrado[['title', 'price']])

#filtro por faixa de preco
min_preco, max_preco  = int(df["price"].min()), int(df["price"].max())
faixa = st.slider("filtrar por faixa de preco (R$)", min_preco, max_preco, (min_preco, max_preco), strp=50)
df_filtrado = df_filtrado[(df["price"] >= faixa[0]) & (df_filtrado["price"] <= faixa[1])]


# colunas como "preco_original" voce pode calcular desconto, sendo que nao coletei o valor ja com desconto com pix, mas isso so trocar o no arquivo magalu_scraper.py

#if "preco_original" in DF.COLUMNS:
#   df_filtrado ["desconto"] = ((df["price_original"] - df["price"]) / df["price_original"]) * 100
#    st.subheader(""📉 Top Descontos")()
#    top_descontos = df_filtrado.sort_value(by="desconto", ascending = False).head(10)
#    st.dataframe(top_descontos[["title", "price","desconto"]])
 
    