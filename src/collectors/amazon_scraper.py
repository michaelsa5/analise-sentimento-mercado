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
NUM_PAGINAS = 5

# Listas para armazenar os dados
todos_titulos = []
todos_precos = []

# Loop nas páginas
for pagina in range(1, NUM_PAGINAS + 1):
    print(f"Coletando dados da página {pagina}...")
    url = f"https://www.amazon.com.br/s?i=electronics&rh=n%3A16243890011&s=popularity-rank&fs=true&qid=1745167691&xpid=yVSyWLo0PcabJ&ref=sr_pg_{pagina}"
    driver.get(url)
    
    # Aguarda o carregamento dos elementos
    time.sleep(5)
    
    # Coleta os elementos
    titulos = [el.text for el in driver.find_elements("xpath", '//div[@data-cy="title-recipe"]//h2//span')]

    precos = [el.text for el in driver.find_elements("xpath", '//span[@class="a-price-whole"]')]
    
    # Alinha o tamanho das listas
    min_len = min(len(titulos), len(precos))
    titulos = titulos[:min_len]
    precos = precos[:min_len]
    
    # Adiciona à lista geral
    todos_titulos.extend(titulos)
    todos_precos.extend(precos)

# Fecha navegador
driver.quit()
service.stop()

# Cria o DataFrame
df = pd.DataFrame({
    'title': todos_titulos,
    'price': todos_precos
})

# Extrai a segunda palavra do título para criar a coluna 'modelo'
df['modelo'] = df['title'].str.split().str[1]

# Salva o DataFrame no arquivo CSV
df.to_csv("./data/raw/amazon_produtos_paginas.csv", index=False, encoding='utf-8-sig')

print(f"\n✅ Coleta finalizada! {len(df)} produtos salvos no arquivo 'amazon_produtos_paginas.csv'")