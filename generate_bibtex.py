#%%
import json

db_path = "../data/mtla.json"
d = json.load(open(db_path))
d
# %%
# import requests

# resp = requests.get(
#     "https://scholar.googleusercontent.com/scholar.bib?q=info:z7nFZipjassJ:scholar.google.com/&output=citation&scisdr=CgWrfB9sEOzsvDqDbjs:AAGBfm0AAAAAYbeFdjtF_nJRC2jw1an0-HDy0EtJkEQA&scisig=AAGBfm0AAAAAYbeFduDm7Gms6RH8jElUjTLPSpGKFjcd&scisf=4&ct=citation&cd=-1&hl=en",
#     headers={
#         "referer": "https://scholar.google.com/",
#         "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
#     },
# )
# resp.content
"""
x-client-data: CI+2yQEIpbbJAQjBtskBCKmdygEIm+zKAQjq8ssBCJ75ywEI1vzLAQjnhMwBCLWFzAEIy4nMAQj9jMwBCKyOzAEI247MAQjSj8wBCNmQzAEIy5LMARiMnssB
Decoded:
message ClientVariations {
  // Active client experiment variation IDs.
  repeated int32 variation_id = [3300111, 3300133, 3300161, 3313321, 3323419, 3340650, 3341470, 3341910, 3342951, 3343029, 3343563, 3343997, 3344172, 3344219, 3344338, 3344473, 3344715];
  // Active client experiment variation IDs that trigger server-side behavior.
  repeated int32 trigger_variation_id = [3329804];
}"""
# %%
import time
import sqlite3
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# %%

driver.get("https://scholar.google.com")
# %%

driver.get(
    "https://scholar.google.com/scholar?start=0&hl=en&as_sdt=0%2C5&q=mountain+torrent&btnG="
)
# %%


def get_bibtex(title):
    query = title.replace(" ", "+")
    driver.get(
        f"https://scholar.google.com/scholar?start=0&hl=en&as_sdt=0%2C5&q={query}&btnG="
    )

    time.sleep(1)
    one_block = driver.find_elements(
        By.CSS_SELECTOR, "div#gs_res_ccl_mid div.gs_r.gs_or.gs_scl"
    )[0]
    cite_button = one_block.find_elements(By.CSS_SELECTOR, "div.gs_fl")[
        -1
    ].find_elements(By.TAG_NAME, "a")[1]
    cite_button.click()
    time.sleep(1)
    bibtex_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#gs_citi a.gs_citi"))
    )
    print(bibtex_button.text)
    # bibtex_button = self.driver.find_element(
    #     By.CSS_SELECTOR, "div#gs_citi a"
    # )
    bibtex_button.click()
    bibtex = driver.find_element(By.TAG_NAME, "html").text
    return bibtex


#%%
title = d[0]["TITLE"]
bibtex = get_bibtex(title)
d[0]["BIBTEX"] = bibtex
d[0]["BIBTEX"]
# %%
import time
from tqdm import tqdm

start = 0
#%%
# start = i
#%%
for i in tqdm(range(start, len(d))):
    start = i
    title = d[i]["TITLE"]
    bibtex = get_bibtex(title)
    d[i]["BIBTEX"] = bibtex
    time.sleep(3)
# %%
json.dump(d, open("../data/mtla.json", "w"))
# %%
db_path = "../data/mtdm.json"
d = json.load(open(db_path))

#%%
file = open("selected.bib", "a+")

# %%
for one in d:
    file.write(one["BIBTEX"])
    file.write("\n")
# %%
file.close()
# %%
d[-1]
# %%
