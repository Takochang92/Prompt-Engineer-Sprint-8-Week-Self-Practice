import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("result.csv")
df.columns = ["時間", "價格"]
df["時間"] = pd.to_datetime(df["時間"])
df["價格"] = df["價格"].astype(float)
df["漲跌"] = df["價格"].diff()
print(df.dtypes)
print(df)

df.plot(x="時間", y="價格", title="BTC Price Over Time")
plt.tight_layout()
plt.savefig("btc_chart.png", dpi=150)
plt.savefig("btc_chart.pdf")
print("圖表已儲存為 btc_chart.png")
