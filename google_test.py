# 不在乎速度，使用本机chrome在线电脑操作
# 能使用本机VPN访问Google即可
#%%

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Use the `install()` method to set `executabe_path` in a new `Service` instance:
service = Service(executable_path=ChromeDriverManager().install())
#%%
# Pass in the `Service` instance with the `service` keyword:
driver = webdriver.Chrome(service=service)

# %%
driver.get("https://scholar.google.com")

# %%
# 遇到了验证是否是机器人的界面，人工进行验证完成
driver.find_element(By.ID, "gs_hdr_tsi").send_keys("mountain torrent")

driver.find_element(By.ID, "gs_hdr_tsb").click()

# %%
el_list = driver.find_elements(
    By.CSS_SELECTOR, "div#gs_res_ccl_mid div.gs_r.gs_or.gs_scl"
)
# %%
try:
    pdf_href = (
        el_list[1]
        .find_element(By.CSS_SELECTOR, "div.gs_or_ggsm a")
        .get_attribute("href")
    )
except:
    pdf_href = ""
pdf_href
# %%
title = el_list[0].find_element(By.TAG_NAME, "h3").text
#%%
main_href = el_list[0].find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href")
main_href
#%%
author = el_list[0].find_element(By.CSS_SELECTOR, "div.gs_a").text
author
# %%
abstract = el_list[0].find_element(By.CSS_SELECTOR, "div.gs_rs").text
abstract

# %%

cite_num = el_list[0].find_elements(By.CSS_SELECTOR, "div.gs_fl")[1].text
# %%
cite_num
# %%
cite_button = (
    el_list[0]
    .find_elements(By.CSS_SELECTOR, "div.gs_fl")[1]
    .find_elements(By.TAG_NAME, "a")[1]
)
cite_button

# %%
cite_button.click()
# %%
bibtex_button = driver.find_element(By.CSS_SELECTOR, "div#gs_citi a")
bibtex_button
# %%
bibtex_button.click()
# %%
bibtex = driver.find_element(By.TAG_NAME, "html").text
bibtex
# %%
driver.back()
# %%
cit_x_button = driver.find_element(By.ID, "gs_cit-x")
cit_x_button
# %%
cit_x_button.click()
# %%
driver.get(
    "https://scholar.google.com/scholar?start=0&hl=en&as_sdt=0%2C5&q=mountain+torrent&btnG="
)
# %%
driver.close()
# %%
