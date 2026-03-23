import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("result.csv")
df.columns = ["時間", "價格"]
df["價格"] = df["價格"].astype(float)

df.plot(x="時間", y="價格", title="BTC Price Over Time")
plt.tight_layout()
plt.savefig("btc_chart.png")
print("圖表已儲存為 btc_chart.png")
