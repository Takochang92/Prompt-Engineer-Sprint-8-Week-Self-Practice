# Week 1 — Day 1 & Day 2 學習筆記

---

## Import — 取用工具

```python
import requests
import csv
from datetime import datetime
import logging
```

- `import xxx` — 取用 Python 內建或安裝的工具
- `from xxx import ooo` — 取用 xxx 模組中的 ooo 功能

| 工具 | 用途 |
|------|------|
| `requests` | 取用 requests 功能，進行 API 操作 |
| `csv` | 取用 csv 功能，進行 csv 檔案的讀寫與儲存 |
| `from datetime import datetime` | 取用 datetime 模組中的 datetime 功能，獲得時間（模組名稱沒有 s）|
| `logging` | 取用 logging 功能，將結果記錄在檔案中，取代 print。因為 print 只會印在終端機，程式關掉就消失 |

---

## URL 宣告

```python
url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
```

寫在最上面先宣告，後續程式碼都可以用 `url` 代稱，不用每次貼完整網址。

---

## 獲取 API 資料

```python
response = requests.get(url, timeout=10)
response.raise_for_status()
```

- `requests.get(url)` — 用 GET 方式發送請求到那個網址
- `timeout=10` — 如果 10 秒內對方沒回應，就放棄，不要一直等
- `response` — 把對方回傳的東西（狀態碼 + 資料）存進這個變數

`raise_for_status()` 負責檢查對方回應是不是成功的。API 回應了不代表成功，HTTP 有狀態碼：

| 狀態碼 | 意思 |
|--------|------|
| `200` | 成功 |
| `404` | 找不到這個資源 |
| `500` | 對方伺服器出錯 |

這行的意思是「如果狀態碼不是 200，主動丟出錯誤」，讓下面的 `except HTTPError` 接住。不寫這行的話，404 或 500 也會被當成成功，你拿到一個失敗的回應卻不知道。

---

## 解析 API 資料

```python
data = response.json()
price = data["data"]["amount"]
```

- `response.json()` — 將 API 回傳的 JSON 資料轉成 Python 可以操作的字典格式
- `data["data"]["amount"]` — 從字典中取出價格，路徑依照每個資料來源的結構而不同

---

## 寫入 CSV

```python
with open("result.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["時間", "價格"])
    writer.writerow([datetime.now(), price])
```

- `with ... as f` — 做完這件事自動關閉檔案，不用手動 close
- `open("result.csv", "w")` — 開啟檔案並以寫入模式存入新紀錄
- `csv.writer(f)` — 建立寫入 CSV 格式的工具
- `writer.writerow([...])` — 寫入一行資料，list 中每個元素變成一個欄位
- `datetime.now()` — 取得現在的時間（`.` 不是 `,`）

---

## try / except — 讓程式出錯不會死掉

```python
try:
    # 有可能出錯的程式碼放這裡
except requests.exceptions.ConnectionError:
    logging.error("連線錯誤")
except requests.exceptions.HTTPError as e:
    logging.error(f"API 錯誤：{e}")
except Exception as e:
    logging.error(f"未知錯誤：{e}")
```

- `try` — 把**有可能出錯的程式碼**放在這裡（不是所有程式碼，import、url 宣告這些不會出錯的放外面）
- `except` — 出錯後抓住錯誤，告訴終端發生了什麼，程式不會直接死掉

| except 對象 | 抓哪種錯 | 什麼情況發生 |
|-------------|---------|------------|
| `ConnectionError` | 連不上 | 網路斷線、對方伺服器沒開 |
| `HTTPError` | 連上但失敗 | 404、500 等狀態碼 |
| `Exception` | 其他所有錯 | 意料之外的狀況 |

---

## logging — 記錄程式的操作內容

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("fetch.log"),
        logging.StreamHandler()
    ]
)
```

- `basicConfig` — 必須放在所有 logging 呼叫的**最上方**，才能讓後續的 logging 依照設定執行

**level — 記錄等級**

| 等級 | 用途 |
|------|------|
| `DEBUG` | 開發時的細節紀錄 |
| `INFO` | 正常運作的紀錄 |
| `WARNING` | 系統有異常，但沒有壞掉 |
| `ERROR` | 系統出錯了 |
| `CRITICAL` | 整個系統掛了 |

**format — 決定每行 log 長什麼樣子**

| 格式 | 顯示內容 |
|------|---------|
| `%(asctime)s` | 時間 |
| `[%(levelname)s]` | 等級名稱（`[]` 是自己加的，會直接顯示在輸出中）|
| `%(message)s` | 程式回傳的訊息 |

---

## Git 指令

| 指令 | 用途 |
|------|------|
| `git add .` | 把所有變更加入暫存區（`add` 和 `.` 中間要有空格）|
| `git add 檔案名稱` | 只加入特定檔案 |
| `git commit -m "訊息"` | 把暫存區的變更存成一個版本 |
| `git push` | 把本地的版本推上 GitHub |
| `git pull` | 把 GitHub 上的版本拉下來同步 |

---

## Terminal 指令

| 指令 | 用途 |
|------|------|
| `pip3 install requests` | 讓 venv 環境安裝 requests（`pip` 無法使用時改用 `pip3`）|
| `cat 檔案名稱` | 在終端機確認某個檔案的內容 |
| `cd ..` | 回到上一層資料夾 |
| `cd 資料夾名稱` | 進入該資料夾 |

**路徑觀念：** 在哪個資料夾下指令，就只會影響那個資料夾裡的檔案。`git add` 只會抓到你目前所在資料夾的檔案，要先確認自己在對的位置。

---

## vim 編輯器

Git merge 時會自動開啟 vim，離開方式：

```
Esc → :wq → Enter
```

- `Esc` — 離開編輯模式
- `:wq` — 儲存並離開（write + quit）
