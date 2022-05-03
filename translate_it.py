#%%
import requests

import hashlib

appid = "20200424000428889"
secret_key = "mPZzhlZ6o6qLqlw7nhXG"
salt = 1435660288
query = "apple"
conc = f"{appid}{query}{salt}{secret_key}"
hl = hashlib.md5()
hl.update(conc.encode(encoding="utf-8"))
sign = hl.hexdigest()
url = f"https://fanyi-api.baidu.com/api/trans/vip/translate?q={query}&from=en&to=zh&appid={appid}&salt={salt}&sign={sign}"
resp = requests.get(url)
resp.content
# %%

import json

d = json.loads(resp.content)
# %%
d["trans_result"][0]["dst"]
# %%
def get_translated(query):
    conc = f"{appid}{query}{salt}{secret_key}"
    hl = hashlib.md5()
    hl.update(conc.encode(encoding="utf-8"))
    sign = hl.hexdigest()
    url = f"https://fanyi-api.baidu.com/api/trans/vip/translate?q={query}&from=en&to=zh&appid={appid}&salt={salt}&sign={sign}"
    resp = requests.get(url)
    d = json.loads(resp.content)
    return d["trans_result"][0]["dst"]


get_translated(
    "\u2026 Taking Linqu County in Shandong Province for an example, the values of warning rainfall\nand transfer rainfall have been given and its isoline are plotted with ArcGIS software, which\nprovides scientific basis for preventing meteorological forecasting of torrential flood disaster. \u2026"
)

# %%
left_d = json.load(open("../data/left.json"))
# %%
def get_cite_str(one):
    token = ""
    if len(one["BIBTEX"]) > 0:
        token = one["BIBTEX"].split("{")[1].split(",")[0]
    return "\\cite{" + token + "}"


print(get_cite_str(left_d[0]))
# %%
res_list = []
for one in left_d:
    en = one["ABSTRACT"]
    zh = get_translated(en)
    cit = get_cite_str(one)
    res_list.append(cit + zh)

# %%
with open("../data/translated.txt", "w") as file:
    file.write("\n".join(res_list))
# %%
