import pandas as pd

# 예제 데이터
data = {
    "TEXT": ["  Oracle DB  ", "  Hello World  "]
}

df = pd.DataFrame(data)
# 양쪽 공백 제거 (TRIM)
df["TRIM"] = df["TEXT"].str.strip()

print(df)
