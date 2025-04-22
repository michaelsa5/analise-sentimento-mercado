import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Caminho para o ChromeDriver
driver_path = "C:/Users/Michael/Downloads/chromedriver_win32/chromedriver.exe"

# Configurações do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Inicia o serviço
service = Service(driver_path)
service.start()

# Cria o WebDriver remoto
driver = webdriver.Remote(service.service_url, options=chrome_options)

# Número de páginas que deseja coletar
NUM_PAGINAS = 3

# Listas para armazenar os dados
todos_titulos = []
todos_precos = []
todos_marcas = []

# Loop nas páginas
for pagina in range(1, NUM_PAGINAS + 1):
    print(f"Coletando dados da página {pagina}...")
    url = f"https://www.magazineluiza.com.br/celulares-e-smartphones/l/te/entity---smartphone/?page={pagina}"
    driver.get(url)
    
    # Aguarda o carregamento dos elementos
    time.sleep(10)
    
    # Coleta os elementos
    titulos = [el.text for el in driver.find_elements("xpath", '//h2[@data-testid="product-title"]')]
    precos = [el.text for el in driver.find_elements("xpath", '//p[@data-testid="price-value"]')]
    marcas = [el.get_attribute("data-brand") for el in driver.find_elements("xpath", '//a[@data-brand]')]

    
    # Alinha o tamanho das listas
    min_len = min(len(titulos), len(precos),len(marcas))
    titulos = titulos[:min_len]
    precos = precos[:min_len]
    marcas = marcas[:min_len]
    
    # Adiciona à lista geral
    todos_titulos.extend(titulos)
    todos_precos.extend(precos)
    todos_marcas.extend(marcas)

# Fecha navegador
driver.quit()
service.stop()

# Cria o DataFrame e salva
df = pd.DataFrame({
    'title': todos_titulos,
    'price': todos_precos,
    'marcas': todos_marcas
})
df.to_csv("./data/raw/magalu_produtos_paginas.csv", index=False, encoding='utf-8-sig')

print(f"\n✅ Coleta finalizada! {len(df)} produtos salvos no arquivo 'magalu_produtos_paginas.csv'")
