from pytrends.request import TrendReq
import pandas as pd

def get_trends(marcas=["Samsung", "Xiaomi", "Motorola"], geo='BR'):
    pytrends = TrendReq(hl='pt-BR', tz=360)

    pytrends.build_payload(marcas, cat=0, timeframe='now 7-d', geo=geo)
    data = pytrends.interest_over_time()

    if 'isPartial' in data.columns:
        data = data.drop(columns=['isPartial'])

    data.to_csv("data/raw/tendencias_google.csv")
    print(data.tail())


if __name__ == "__main__":
    get_trends()
