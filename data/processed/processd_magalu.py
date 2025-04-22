import pandas as pd
import re

# Carregar os dados
file_path = "./data/raw/magalu_produtos_paginas.csv"
df = pd.read_csv(file_path)

# Função para limpar preços
def clean_price(price):
    if isinstance(price, str):
        # Remove "ou R$" e converte para float
        price = price.replace("ou R$", "").replace(".", "").replace(",", ".").strip()
        try:
            return float(price)
        except ValueError:
            return None
    return None

# Função para padronizar marcas
def standardize_brand(brand):
    brand_map = {
        "samsung": "Samsung",
        "apple": "Apple",
        "xiaomi": "Xiaomi",
        "motorola": "Motorola",
        "realme": "Realme",
        "infinix": "Infinix",
        "oppo": "Oppo",
        "positivo": "Positivo",
        "navcity": "Navcity",
        "tlc": "TLC",
        "tablet": "Tablet",
        "unity": "Unity",
        "zte": "ZTE",
        "lg": "LG",
        "asus": "Asus",
        "cubot": "Cubot",
        "jys": "JYS",
        "morotola": "Motorola",
        "X6" : "Xiaomi",
        "X7" : "Xiaomi",
        "C75" : "C75" # Correção de erro de digitação
    }
    return brand_map.get(brand.lower(), brand.capitalize())

# Limpar preços
df["price"] = df["price"].apply(clean_price)

# Padronizar marcas
df["marcas"] = df["marcas"].apply(standardize_brand)

# Remover registros sem preço
df = df.dropna(subset=["price"])

# Remover duplicatas
df = df.drop_duplicates(subset=["title", "price"])

# Resetar índice
df = df.reset_index(drop=True)

# Salvar o DataFrame normalizado
output_path = "data/processed/magalu_phones_clean.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"✅ Dados normalizados salvos em: {output_path}")