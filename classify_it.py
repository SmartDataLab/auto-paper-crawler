# use LDA topic model to classify the document and
#%%
import pandas as pd
import json

data_list = []
d = json.load(open("../data/mtdm.json"))
data_list += [
    {"id": i, "content": one["TITLE"] + one["ABSTRACT"]} for i, one in enumerate(d)
]
d = json.load(open("../data/mtla.json"))
data_list += [
    {"id": i, "content": one["TITLE"] + one["ABSTRACT"]} for i, one in enumerate(d)
]
d = json.load(open("../data/hydrological+machine+learning.json"))
data_list += [
    {"id": i, "content": one["TITLE"] + one["ABSTRACT"]} for i, one in enumerate(d)
]
d = json.load(
    open("../data/mountain+torrent+hydrological+artificial+intelligence.json")
)
data_list += [
    {"id": i, "content": one["TITLE"] + one["ABSTRACT"]} for i, one in enumerate(d)
]
# %%
df = pd.DataFrame(data_list)
# %%
df
# %%

df.to_excel("../../LDA_TOPICMODELING/input.xls")
# %%
# d = json.load(open("../data/mtdm.json"))
df_class = pd.read_csv("../../LDA_TOPICMODELING/lda_result/res_doc_topic.csv")
df_class
# %%
import numpy as np

columns = list(df_class.columns)[1:]
columns
#%%
np.array(df_class[columns])
# %%
df["class"] = np.argmax(np.array(df_class[columns]), axis=1)
# %%
df["class"]
# %%
df["query"] = (
    ["mtdm"] * len(json.load(open("../data/mtdm.json")))
    + ["mtla"] * len(json.load(open("../data/mtla.json")))
    + ["hydrological+machine+learning"]
    * len(json.load(open("../data/hydrological+machine+learning.json")))
    + ["mountain+torrent+hydrological+artificial+intelligence"]
    * len(
        json.load(
            open("../data/mountain+torrent+hydrological+artificial+intelligence.json")
        )
    )
)

# %%
df["main_href"] = (
    [one["MAIN_HERF"] for one in json.load(open("../data/mtdm.json"))]
    + [one["MAIN_HERF"] for one in json.load(open("../data/mtla.json"))]
    + [
        one["MAIN_HERF"]
        for one in json.load(open("../data/hydrological+machine+learning.json"))
    ]
    + [
        one["MAIN_HERF"]
        for one in json.load(
            open("../data/mountain+torrent+hydrological+artificial+intelligence.json")
        )
    ]
)
#%%
df["pdf_href"] = (
    [one["PDF_HERF"] for one in json.load(open("../data/mtdm.json"))]
    + [one["PDF_HERF"] for one in json.load(open("../data/mtla.json"))]
    + [
        one["PDF_HERF"]
        for one in json.load(open("../data/hydrological+machine+learning.json"))
    ]
    + [
        one["PDF_HERF"]
        for one in json.load(
            open("../data/mountain+torrent+hydrological+artificial+intelligence.json")
        )
    ]
)
#%%
df.to_excel("../data/class_result.xls")
# %%
df