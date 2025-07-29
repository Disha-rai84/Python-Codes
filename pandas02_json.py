import pandas as pd


df = pd.read_json("data.json")


print(df.to_string())
# print(pd.options.display.max_rows)