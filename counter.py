import pandas as pd
import os
p = os.getcwd()
files = os.listdir(p)
size = 0
for file in files:
    if file.find(".py") != -1:
        continue
    df = pd.read_csv(f"{p}\\{file}")
    size += df.shape[0]
print(size)