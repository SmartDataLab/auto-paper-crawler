#%%
import sqlite3

conn = sqlite3.connect("../data/paper.db")
#%%
import json

json_path = "../data/mountain+torrents+loss+assessment.json"
d = json.load(open(json_path))
d[0]
# %%
for one in d:
    c = conn.cursor()
    c.execute("INSERT INTO FIRST_FILTER (TITLE) VALUES(?);", (one["TITLE"],))
conn.commit()
# %%
