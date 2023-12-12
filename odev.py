import requests
url = "https://api.coindcx.com/exchange/v1/markets_details"
response = requests.get(url)
data = response.json()
#USDT ile ilgili olanları filtrele
usdt_data = [market for market in data if 'USDT' in market.get('symbol', '')]

# Filtrelenmiş verileri ekrana yazdır
for market in usdt_data:
    print(f"Symbol: {market['symbol']}")
    print(f"Min Price: {market.get('min_price', 'N/A')}")
    print(f"Max Price: {market.get('max_price', 'N/A')}")
    print("---------")
