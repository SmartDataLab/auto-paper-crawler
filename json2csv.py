#%%
import json
import pandas as pd

json_path = "../data/mountain+torrents+disaster+monitor.json"
d = json.load(open(json_path))
#%%
df = pd.DataFrame(d)
df
# %%
df.to_csv("../data/mountain+torrents+disaster+monitor.csv")
# %%
