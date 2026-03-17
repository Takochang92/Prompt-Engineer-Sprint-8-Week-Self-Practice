import requests
data = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot").json()
print(data)
