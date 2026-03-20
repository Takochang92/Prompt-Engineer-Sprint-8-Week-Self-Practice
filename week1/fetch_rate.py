import schedule
import time
import requests
import csv
import logging
from datetime import datetime


logging.basicConfig(
  level=logging.INFO,
  format= "%(asctime)s [%(levelname)s] %(message)s",
  handlers=[
    logging.FileHandler("fetch.log"),
    logging.StreamHandler()
  ]
)

with open("result.csv", "w", newline="") as f:
  writer = csv.writer(f)
  writer.writerow(["時間", "價格"])


def job():
  url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    price = data["data"]["amount"]

    with open("result.csv", "a", newline="") as f:
      writer = csv.writer(f)
      writer.writerow([datetime.now(), price])

    logging.info(f"完成！價格：{price}")

  except requests.exceptions.ConnectionError:
    logging.error("連線錯誤，請確認連線狀態")
  except requests.exceptions.HTTPError as e:
    logging.error(f"API 錯誤：{e}")
  except Exception as e:
    logging.error(f"未知錯誤：{e}")


schedule.every(5).minutes.do(job)

while True:
  schedule.run_pending()
  time.sleep(1)



