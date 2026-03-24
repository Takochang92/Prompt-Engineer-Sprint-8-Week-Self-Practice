# Questions Log — Prompt Engineer Sprint

---

## Week 1 · Day 5

| # | 問題 | 重點答案 |
|---|------|---------|
| 1 | `.env` 檔案的用途是什麼？為什麼不能把 API 金鑰直接寫在程式碼裡？ | 重要資訊存在本機，避免推上 GitHub 後被任何人取得 |
| 2 | `.gitignore` 裡寫了 `.env`，但 `git status` 還是看得到它，最可能的原因是什麼？ | `.env` 已經被 commit 過，Git 持續追蹤。用 `git rm --cached .env` 解除追蹤 |
| 3 | `os.getenv("FETCH_INTERVAL")` 回傳的是什麼型別？為什麼需要加 `int()`？ | 回傳 `str`，`schedule.every()` 需要數字，不轉型會報錯 |
| 4 | `schedule.every(5).minutes.do(job)` 放在 `def job()` 之前會發生什麼事？ | Python 從上到下執行，`job` 還未定義，直接 `NameError` 停掉 |
| 5 | `url = os.getenv("API_URL")` 應該放在 `job()` 外面還是裡面？為什麼？ | 外面。全域設定只需讀取一次，放裡面會每次執行都重複讀取 |
| 6 | `"w"` 和 `"a"` 模式的差別？這支程式各用在哪裡？ | `"w"` 覆蓋，用於寫標題列；`"a"` 累積，用於寫每筆價格資料 |
| 7 | `global last_price` 的作用是什麼？拿掉會發生什麼事？ | 修改函式外的變數。拿掉後每次執行只改局部變數，函式結束就消失，警報永遠不觸發 |
| 8 | `logging.warning` 和 `logging.error` 的差別？各用在哪個情境？ | `WARNING` = 程式正常但資料有異常（價格波動 > 1%）；`ERROR` = 任務失敗（API 連線錯誤） |
| 9 | `job()` 在這支程式裡被呼叫幾次？分別在哪裡？ | 兩次：啟動時手動呼叫一次（立即執行）；`schedule` 登記後每 5 分鐘自動觸發 |
| 10 | `load_dotenv()` 沒寫的話 `os.getenv("API_URL")` 會回傳什麼？程式會怎樣？ | 回傳 `None`。`int(None)` 直接 `TypeError`，程式在讀 `FETCH_INTERVAL` 那行就停掉 |

---

## Week 1 · Day 4

| # | 問題 | 重點答案 |
|---|------|---------|
| 1 | `pd.read_csv()` 讀進來的數字是什麼型別？要怎麼轉成可以計算的數字？ | 預設是 `str`，用 `astype(float)` 轉換 |
| 2 | `df.columns = ["時間", "價格"]` 的用途是什麼？ | 設定欄位名稱，之後才能用 `df["價格"]` 指定該欄 |
| 3 | `plt.savefig()` 和 `plt.show()` 的差別？ | `savefig` 存檔不跳視窗；`show` 跳視窗不存檔；兩個都寫則都執行，`show` 放後面 |
| 4 | `dpi` 是什麼？預設值是多少？ | 解析度，預設 100，`dpi=150` 輸出更清晰 |
| 5 | `df["漲跌"] = df["價格"].diff()` 做了什麼事？ | 新增一欄，每筆資料與前一筆的差值 |
| 6 | `pd.to_datetime()` 的用途是什麼？ | 把文字格式的時間轉成 datetime 型別，才能正確排序和畫圖 |
| 7 | `strftime("%d %b %Y")` 會輸出什麼格式？ | 例：`24 Mar 2026` |
| 8 | `%b` 和 `%m` 的差別是什麼？ | `%b` 是月份縮寫（Mar）；`%m` 是月份數字（03） |
| 9 | 為什麼 `schedule` 啟動後要先呼叫一次 `job()`？ | 預設要等滿設定時間才第一次執行，先呼叫一次可以立即取得第一筆資料 |
| 10 | PNG 和 PDF 格式各適合用在什麼場合？ | PNG：網頁、報告截圖；PDF：印刷、正式文件 |

---

## Week 1 · Day 3

| # | 問題 | 重點答案 |
|---|------|---------|
| 1 | `schedule.every(5).minutes.do(job)` 和 `while True` 各自的作用是什麼？ | `schedule` 登記任務；`while True` 讓程式持續運行 |
| 2 | `run_pending()` 和 `run.pending()` 哪個正確？ | `run_pending()`，底線不是點 |
| 3 | CSV `"w"` 模式的問題是什麼？ | 每次執行都覆蓋整個檔案，只保留最後一筆資料 |
| 4 | `global` 關鍵字的用途是什麼？ | 讓函式內可以修改函式外的變數 |
| 5 | `logging.basicConfig` 放在 `job()` 裡面會有什麼問題？ | 每次執行都重新設定，造成 log 重複輸出 |

---

## Week 1 · Day 2

| # | 問題 | 重點答案 |
|---|------|---------|
| 1 | `try/except` 的用途是什麼？ | 捕捉錯誤，程式出錯不會直接停掉 |
| 2 | `ConnectionError` 和 `HTTPError` 分別抓哪種錯？ | `ConnectionError`：連不上；`HTTPError`：連上但 API 回傳錯誤狀態碼 |
| 3 | `logging` 取代 `print` 的好處是什麼？ | 可同時輸出到 Terminal 和寫入 log 檔，並附上時間和等級 |
| 4 | `raise_for_status()` 的作用是什麼？ | 收到非 200 狀態碼時自動拋出 `HTTPError` |
| 5 | logging 的五個等級由低到高是什麼？ | DEBUG → INFO → WARNING → ERROR → CRITICAL |
