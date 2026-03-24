# Learning Note — Prompt Engineer Sprint

---

## Week 1 · Day 1

### venv 虛擬環境

```bash
python3 -m venv venv        # 建立虛擬環境
source venv/bin/activate    # 啟動虛擬環境
deactivate                  # 關閉虛擬環境
```

- 每個專案獨立安裝套件，不會互相干擾
- 啟動後 Terminal 前面會出現 `(venv)` 字樣

---

## Week 1 · Day 2

### CSV 寫入

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

### try / except — 讓程式出錯不會死掉

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

- `try` — 把**有可能出錯的程式碼**放在這裡（import、url 宣告這些不會出錯的放外面）
- `except` — 出錯後抓住錯誤，告訴終端發生了什麼，程式不會直接死掉

| except 對象 | 抓哪種錯 | 什麼情況發生 |
|-------------|---------|------------|
| `ConnectionError` | 連不上 | 網路斷線、對方伺服器沒開 |
| `HTTPError` | 連上但失敗 | 404、500 等狀態碼 |
| `Exception` | 其他所有錯 | 意料之外的狀況 |

---

### logging — 記錄程式的操作內容

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

- `basicConfig` — 必須放在所有 logging 呼叫的**最上方**

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

### Git 指令

| 指令 | 用途 |
|------|------|
| `git add .` | 把所有變更加入暫存區（`add` 和 `.` 中間要有空格）|
| `git add 檔案名稱` | 只加入特定檔案 |
| `git commit -m "訊息"` | 把暫存區的變更存成一個版本 |
| `git push` | 把本地的版本推上 GitHub |
| `git pull` | 把 GitHub 上的版本拉下來同步 |

---

### Terminal 指令

| 指令 | 用途 |
|------|------|
| `pip3 install 套件名稱` | 安裝套件（`pip` 無法使用時改用 `pip3`）|
| `cat 檔案名稱` | 在終端機確認某個檔案的內容 |
| `cd ..` | 回到上一層資料夾 |
| `cd 資料夾名稱` | 進入該資料夾 |
| `tail -f 檔案名稱` | 即時監看檔案，有新內容自動顯示 |

**路徑觀念：** 在哪個資料夾下指令，就只會影響那個資料夾裡的檔案。`source venv/bin/activate` 要在專案**根目錄**下執行。

---

### vim 編輯器

Git merge 時會自動開啟 vim，離開方式：

```
Esc → :wq → Enter
```

- `Esc` — 離開編輯模式
- `:wq` — 儲存並離開（write + quit）

---

## Week 1 · Day 3

### schedule — 定時自動執行

```python
import schedule
import time

schedule.every(5).minutes.do(job)  # 每 5 分鐘執行一次 job()

while True:
    schedule.run_pending()  # 檢查有沒有到時間要執行的任務
    time.sleep(1)           # 每秒檢查一次
```

- `schedule.every(5).minutes.do(job)` — 登記任務，每 5 分鐘跑一次
- `while True` — 讓程式持續運行，Terminal 關掉就停了
- `run_pending()` — 底線，不是 `run.pending()`

---

### CSV 兩種寫入模式

| 模式 | 用途 |
|------|------|
| `"w"` | 覆蓋，每次重新開始，用來**寫標題列**（只執行一次） |
| `"a"` | 累積（append），每次新增一行，用來**寫資料** |

正確做法：標題列在程式啟動時用 `"w"` 寫一次，資料在 `job()` 裡用 `"a"` 累積。

---

### global 變數 — 在函式之間共享狀態

```python
last_price = None  # 函式外定義

def job():
    global last_price  # 宣告要使用外部的 last_price
    ...
    last_price = price  # 更新，下次 job() 執行時可以讀到
```

- 沒有 `global` 宣告，函式內修改的只是局部變數，外部不會改變

---

### 正確的啟動步驟

```bash
cd ~/projects/Prompt-Engineer-Sprint   # 1. 進到專案根目錄
source week1/venv/bin/activate         # 2. 啟動 venv
cd week1                               # 3. 進到 week1
python3 fetch_rate.py                  # 4. 執行程式
```

---

### 今日比喻

| 指令 | 比喻 |
|------|------|
| `cd ~/projects/...` | 走進工作室 |
| `source .../activate` | 開啟專用工具箱 |
| `python3 fetch_rate.py` | 按下啟動鍵 |
| `tail -f result.csv` | 看即時儀表板 |

---
## Week 1 · Day 4 — 資料分析與視覺化

### pandas & matplotlib

| 套件 | 用途 |
|------|------|
| `pandas` | 處理表格資料 |
| `matplotlib` | 畫圖 |

### DataFrame 操作
```python
df = pd.read_csv("result.csv")       # 讀取 CSV
df.columns = ["時間", "價格"]         # 設定欄位名稱
df["時間"] = pd.to_datetime(df["時間"]) # 文字 → datetime 型別
df["價格"] = df["價格"].astype(float)  # 文字 → 數字
df["漲跌"] = df["價格"].diff()         # 新增欄位：每筆與前筆的差值
print(df.dtypes)                      # 確認每欄的型別
```

### savefig vs show

| 動作 | 結果 |
|------|------|
| `plt.savefig("chart.png")` | 存檔，不跳出視窗 |
| `plt.show()` | 跳出視窗，不存檔 |
| 兩個都寫 | 跳出視窗，也存檔 |

`dpi` = 解析度，預設 100，`dpi=150` 輸出更清晰

### savefig 格式

| 格式 | 適合用在 |
|------|---------|
| PNG | 一般截圖、報告、網頁 |
| PDF | 印刷、正式文件 |
| SVG | 需要縮放的場合 |

### strftime 格式碼

| 格式碼 | 意思 | 範例 |
|--------|------|------|
| `%Y` | 四位數年份 | `2026` |
| `%m` | 月份數字 | `03` |
| `%b` | 月份縮寫 | `Mar` |
| `%d` | 日期 | `23` |
| `%H` | 小時（24h）| `10` |
| `%M` | 分鐘 | `17` |
| `%S` | 秒數 | `37` |
```python
datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # → 2026-03-23 10:17:37
datetime.now().strftime("%d %b %Y")            # → 23 Mar 2026
```

### schedule 啟動沒有動作

預設要等滿設定時間才第一次執行，修正：在 `while True` 前先呼叫一次 `job()`
```python
job()
schedule.every(5).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
```

---
 
## Week 1 · Day 5
 
### dotenv — 環境變數管理
 
```bash
pip3 install python-dotenv
```
 
```python
from dotenv import load_dotenv
import os
 
load_dotenv()               # 讀取 .env 檔案
url = os.getenv("API_URL")  # 取得環境變數的值
```
 
### .env 檔案格式
 
```
API_URL=https://api.coinbase.com/v2/prices/BTC-USD/spot
FETCH_INTERVAL=5
```
 
- 純文字格式，`KEY=VALUE`，不加引號
- 只存在本機，**不推上 GitHub**
 
### .gitignore — 擋住不該上傳的檔案
 
```
.env
week1/venv/
__pycache__/
```
 
- `.env` 放這裡，Git 就看不到它，永遠不會被 commit
 
### 為什麼要用 .env？
 
| 方式 | 風險 |
|------|------|
| 寫死在程式碼裡 | 推上 GitHub 就公開了，任何人都能看到 API 金鑰 |
| 放在 `.env` | 只存在本機，程式從外部讀取，原始碼保持乾淨 |
 
就像把家門鑰匙放在保險箱，而不是刻在門上。
 
### Python 執行順序規則
 
> 先定義，再使用。函式要寫在被呼叫之前。
 
```python
# ❌ 錯誤：job 還沒定義就被登記
schedule.every(5).minutes.do(job)
def job():
    ...
 
# ✅ 正確：先定義 job，再登記
def job():
    ...
schedule.every(5).minutes.do(job)
```
 
### 設定值應該放在哪裡？
 
```python
load_dotenv()
url = os.getenv("API_URL")        # ✅ 放在 job() 外面，只讀一次
interval = int(os.getenv("FETCH_INTERVAL"))
 
def job():
    # url 直接使用，不需要在函式裡重新讀取
    response = requests.get(url, timeout=10)
```
 
- 設定值在程式啟動時讀取一次即可，不需要每次呼叫 `job()` 都重新讀
