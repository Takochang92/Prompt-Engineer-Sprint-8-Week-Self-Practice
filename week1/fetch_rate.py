import requests
import csv
from datetime import datetime

response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")

data = response.json()
print(data)

price = data["data"]["amount"]

with open("result.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerow(["時間", "價格"])
  writer.writerow([datetime.now(), price])

print(f'完成！價格：{price}')

