import pandas as pd
import numpy as np

# 예제 데이터
data = {
    "NUM": [12.34]
}

df = pd.DataFrame(data)

# 소수점 이하 내림
df["내림"] = np.floor(df["NUM"])

print(df)
