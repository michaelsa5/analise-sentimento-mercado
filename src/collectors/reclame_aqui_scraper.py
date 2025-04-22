from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

def get_reputacao_xpath(marca="samsung"):
    url = f"https://www.reclameaqui.com.br/empresa/{marca}/"

    options = Options()
   # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Espera o conteúdo dinâmico carregar

    dados = {}

    try:
        # Nota do consumidor (nota geral)
        nota_xpath = '//*[@id="ra-new-reputation"]/span/b'
        dados["Nota do consumidor"] = driver.find_element(By.XPATH, nota_xpath).text.strip()

        # Reclamações totais
        total_xpath = '//*[@id="newPerformanceCard"]/div[2]/div[1]/span/strong'
        dados["Reclamações recebidas"] = driver.find_element(By.XPATH, total_xpath).text.strip()

        # Reclamações respondidas
        respondidas_xpath = '//*[@id="newPerformanceCard"]/div[2]/div[2]/span/strong'
        dados["Reclamações respondidas"] = driver.find_element(By.XPATH, respondidas_xpath).text.strip()


    except Exception as e:
        print(f"[ERRO] Falha ao extrair dados: {e}")
    finally:
        driver.quit()

    return dados

# Exemplo de uso
if __name__ == "__main__":
    marca = "samsung"
    reputacao = get_reputacao_xpath(marca)
    if reputacao:
        df = pd.DataFrame([reputacao])
        df.to_csv(f"./data/raw/reputacao_{marca}.csv", index=False)
        print(df)

    