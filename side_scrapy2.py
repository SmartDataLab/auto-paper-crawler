# %%
# data missing and need to be retry
import json
import requests
import re


# %%
# stock_id = {}
# for n in range(1, 3):
#     m = str(n)
#     url = "https://guba.eastmoney.com/remenba.aspx?type=1&tab=" + m
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 \
#         (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
#     }
#     html_response = requests.get(url=url, headers=headers)
#     textt = html_response.text
#     textt = textt.replace(
#         '</a></li></ul><div class="more"><a href="javascript:void(0)" target="_self">点击查看更多<span></span></a></div><ul class="ngblistul2 hide"><li><a ',
#         "</a></li><li><a",
#     )
#     textt = textt.replace("</a></li></ul>", "</a></li><li><a")
#     a = re.findall(r'href="list,(.*?)</a></li><li><a', textt)
#     for i in a:
#         if i[-1] == "吧":
#             continue
#         stock_id[i.split(")", 1)[1]] = i[i.index("(") + 1 : i.index(")")]


#%%

#%%
import json

# stock_id = json.load(open("../data/stock_id.json"))
#%%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=ChromeDriverManager().install())
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
d = webdriver.Chrome(service=service)
d.get("https://guba.eastmoney.com/remenba.aspx?type=1&tab=1")
#%%
more_button = d.find_element(By.CSS_SELECTOR, "div.more")
#%%
more_button.click()
# %%
import json

a_list = d.find_elements(By.CSS_SELECTOR, "ul.ngblistul2 li a")
len(a_list)
stock_id = json.load(open("../data/stock_id.json"))
stock_back = {}
for a in a_list:
    id_, name = a.text.replace("(", "").split(")")
    if name not in stock_id.keys():
        stock_back[name] = id_
stock_back
#%%
d.get("https://guba.eastmoney.com/remenba.aspx?type=1&tab=2")
#%%
more_button = d.find_element(By.CSS_SELECTOR, "div.more")
#%%
more_button.click()
# %%
import json

a_list = d.find_elements(By.CSS_SELECTOR, "ul.ngblistul2 li a")
print(len(a_list))

for a in a_list:
    id_, name = a.text.replace("(", "").split(")")
    if name not in stock_id.keys():
        stock_back[name] = id_
len(stock_back)
#%%
with open("../data/stock_back.json", "w") as f:
    json.dump(stock_back, f, ensure_ascii=False)
#%%
# 浏览器初始化

stock_pages = {}
# %%
# 初步，有错误对抗
import time
from tqdm import tqdm

loc = 0
for i in tqdm(list(stock_back.keys())[loc:]):
    try:
        url = "https://guba.eastmoney.com/list," + stock_back[i] + ".html"
        d.get(url)
        time.sleep(0.1)
        sumpage = d.find_element_by_class_name("sumpage")
        stock_pages[i] = sumpage.text
    except Exception as e:
        print(e)
        # loc = list(stock_id.keys()).index(i)
# %%
# 补缺
from tqdm import tqdm

loc = list(stock_back.keys()).index(i) - 1
#%%
#%%
for i in tqdm(list(stock_back.keys())[loc:]):
    try:
        url = "https://guba.eastmoney.com/list," + stock_back[i] + ".html"
        d.get(url)
        time.sleep(0.1)
        sumpage = d.find_element_by_class_name("sumpage")
        stock_pages[i] = sumpage.text
    except Exception as e:
        print(e)
# %%
x = set(stock_back.keys()) - set(stock_pages.keys())
len(x)
#%%
for i in tqdm(list(x)):
    try:
        url = "https://guba.eastmoney.com/list," + stock_back[i] + ".html"
        d.get(url)
        time.sleep(0.1)
        sumpage = d.find_element_by_class_name("sumpage")
        stock_pages[i] = sumpage.text
    except Exception as e:
        print(e)

# %%
x = set(stock_back.keys()) - set(stock_pages.keys())
len(x)
#%%
for i in tqdm(list(x)):
    stock_pages[i] = "1"

#%%
x = set(stock_back.keys()) - set(stock_pages.keys())
len(x)
#%%
# 生成文件
with open("../data/stock_pages_back.json", "w") as f:
    json.dump(stock_pages, f, ensure_ascii=False)
# %%
