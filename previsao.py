import requests
import pandas as pd
from datetime import datetime

API_KEY = "668e4b39a542d623f371c97a3b79148e"
capitais = [
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", "Vitória", "Goiânia",
    "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém", "João Pessoa", "Curitiba", "Recife",
    "Teresina", "Rio de Janeiro", "Natal", "São Paulo", "Porto Alegre", "Florianópolis", "Palmas", "Aracaju"
]

dados_tempo = []

for cidade in capitais:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        clima = dados["weather"][0]["description"].capitalize()
        temp = round(dados["main"]["temp"], 2)
        sensacao = round(dados["main"]["feels_like"], 2)
        umidade = dados["main"]["humidity"]
        vento = round(dados["wind"]["speed"], 2)
        
        dados_tempo.append({
            "Cidade": cidade,
            "Descrição": clima,
            "Temperatura (°C)": temp,
            "Sensação Térmica (°C)": sensacao,
            "Umidade (%)": umidade,
            "Vento (m/s)": vento
        })
    else:
        print(f"Erro ao buscar dados para {cidade}: {resposta.status_code}")

# Criar DataFrame
df = pd.DataFrame(dados_tempo)

# Salvar CSV com dados prontos para Power BI
df.to_csv("clima_capitais_brasil.csv", index=False, sep=";", encoding="utf-8-sig", decimal=",")

