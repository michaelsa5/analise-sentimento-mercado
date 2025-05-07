# src/dashboards/dashboard_streamlit.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados com cache
@st.cache_data
def carregar_dados(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        st.error("Arquivo não encontrado. Certifique-se de que o caminho está correto.")
        return pd.DataFrame()

# Carregar dados
df = carregar_dados("data/processed/magalu_phones_clean.csv")

# Verificar se o dataframe está vazio
if df.empty:
    st.stop()

# Extrair marcas do título
df['marcas'] = df['title'].str.extract(r'(^\w+)', expand=False)

# Título do Dashboard
st.title("📱 Radar Varejo: Análise de Smartphones")

# Filtro de marca
st.sidebar.header("Filtros")
marcas = df['marcas'].value_counts().index.tolist()
marca_selecionada = st.sidebar.multiselect("Filtrar por Marca", marcas, default=marcas[:5])

df_filtrado = df[df['marcas'].isin(marca_selecionada)]

# Filtro por faixa de preço
min_preco, max_preco = int(df["price"].min()), int(df["price"].max())
faixa = st.sidebar.slider("Filtrar por faixa de preço (R$)", min_preco, max_preco, (min_preco, max_preco), step=50)
df_filtrado = df_filtrado[(df_filtrado["price"] >= faixa[0]) & (df_filtrado["price"] <= faixa[1])]

# Verificar se há dados filtrados
if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
    st.stop()

# Gráfico: Distribuição de Preços
st.subheader("Distribuição de Preços")
fig1, ax1 = plt.subplots()
sns.histplot(df_filtrado["price"], bins=20, kde=True, ax=ax1)
ax1.set_xlabel("Preço (R$)")
ax1.set_ylabel("Frequência")
st.pyplot(fig1)

# Gráfico: Preço Médio por Marca
st.subheader("Preço Médio por Marca")
df_group = df_filtrado.groupby("marcas")["price"].mean().sort_values(ascending=False)
fig2, ax2 = plt.subplots()
df_group.plot(kind='bar', color='green', ax=ax2)
ax2.set_ylabel("Preço Médio (R$)")
ax2.set_xlabel("Marca")
st.pyplot(fig2)

# Tabela de Produtos
st.subheader("📋 Tabela de Produtos")
st.dataframe(df_filtrado[['title', 'price']])

# Calcular descontos, se a coluna "price_original" existir
if "price_original" in df.columns:
    df_filtrado["desconto"] = ((df["price_original"] - df["price"]) / df["price_original"]) * 100
    st.subheader("📉 Top Descontos")
    top_descontos = df_filtrado.sort_values(by="desconto", ascending=False).head(10)
    st.dataframe(top_descontos[["title", "price", "desconto"]])

# Rodapé
st.markdown(f"**Total de produtos filtrados: {len(df_filtrado)}**")
#    st.subheader(""📉 Top Descontos")()
#    top_descontos = df_filtrado.sort_value(by="desconto", ascending = False).head(10)
#    st.dataframe(top_descontos[["title", "price","desconto"]])
 
    
