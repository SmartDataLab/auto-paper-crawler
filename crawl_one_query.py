#%%
import time
import sqlite3
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#%%
class AutoScholar(object):
    def __init__(self, driver: WebDriver, db_path) -> None:
        super().__init__()
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.driver = driver
        # make the bot validation pass
        self.driver.get("https://scholar.google.com")

    def crawl(self, query, total_page_num, need_bibtex=False):
        self.query = query.replace(" ", "+")
        for i in range(total_page_num):
            self.crawl_one(i, need_bibtex)

    def crawl_one(self, page_num, need_bibtex):
        self.driver.get(
            f"https://scholar.google.com/scholar?start={page_num * 10}&hl=en&as_sdt=0%2C5&q={self.query}&btnG="
        )
        el_list = self.driver.find_elements(
            By.CSS_SELECTOR, "div#gs_res_ccl_mid div.gs_r.gs_or.gs_scl"
        )
        # self.
        res = {}
        for i, el in enumerate(el_list):
            try:
                pdf_href = el.find_element(
                    By.CSS_SELECTOR, "div.gs_or_ggsm a"
                ).get_attribute("href")
            except:
                pdf_href = ""
            try:
                title = el.find_element(By.TAG_NAME, "h3").text
            except:
                title = ""
            try:
                main_href = el.find_element(By.CSS_SELECTOR, "h3 a").get_attribute(
                    "href"
                )
            except:
                main_href = ""
            try:
                author = el.find_element(By.CSS_SELECTOR, "div.gs_a").text
            except:
                author = ""
            try:
                abstract = el.find_element(By.CSS_SELECTOR, "div.gs_rs").text
            except:
                abstract = ""
            try:
                cite_num = el.find_elements(By.CSS_SELECTOR, "div.gs_fl")[1].text
            except:
                cite_num = ""
            res[i] = {
                "TITLE": title,
                "AUTHOR": author,
                "QUERY": self.query,
                "CITE_NUM": cite_num,
                "ABSTRACT": abstract,
                "MAIN_HERF": main_href,
                "PDF_HERF": pdf_href,
                "BIBTEX": "",
            }

        if need_bibtex:
            for i in res.keys():
                print(i)
                try:
                    cite_button = (
                        self.driver.find_elements(
                            By.CSS_SELECTOR, "div#gs_res_ccl_mid div.gs_r.gs_or.gs_scl"
                        )[i]
                        .find_elements(By.CSS_SELECTOR, "div.gs_fl")[1]
                        .find_elements(By.TAG_NAME, "a")[1]
                    )
                    cite_button.click()
                    time.sleep(1)
                    bibtex_button = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "div#gs_citi a.gs_citi")
                        )
                    )
                    print(bibtex_button.text)
                    # bibtex_button = self.driver.find_element(
                    #     By.CSS_SELECTOR, "div#gs_citi a"
                    # )
                    bibtex_button.click()
                    bibtex = self.driver.find_element(By.TAG_NAME, "html").text
                    res[i]["BIBTEX"] = bibtex
                    self.driver.back()
                    cit_x_button = self.driver.find_element(By.ID, "gs_cit-x")
                    cit_x_button.click()
                except Exception as e:
                    print("fail with ", e)
        c = self.conn.cursor()
        for i, data in res.items():
            sql = "INSERT INTO PAPER (TITLE,AUTHOR,QUERY,CITE_NUM,ABSTRACT,MAIN_HERF,PDF_HERF,BIBTEX) VALUES(?,?,?,?,?,?,?,?);"
            c.execute(
                sql,
                (
                    data["TITLE"],
                    data["AUTHOR"],
                    data["QUERY"],
                    data["CITE_NUM"],
                    data["ABSTRACT"],
                    data["MAIN_HERF"],
                    data["PDF_HERF"],
                    data["BIBTEX"],
                ),
            )
        self.conn.commit()


#%%
# if __name__ == "__main__":
# absolute path = '/Users/su/.wdm/drivers/chromedriver/mac64/100.0.4896.60'
service = Service(executable_path=ChromeDriverManager().install())
# service = Service(
#     executable_path="/Users/su/.wdm/drivers/chromedriver/mac64/100.0.4896.60"
# )
# service = Service(executable_path=ChromeDriverManager())
#%%
driver = webdriver.Chrome(service=service)
#%%
a_s = AutoScholar(driver, "data/troberta.db")
a_s
#%%
# test for crawler connection to google scholar
a_s.driver.get(
    "https://scholar.google.com/scholar?start=0&hl=en&as_sdt=0%2C5&q=mountain+torrent&btnG="
)
#%%
a_s.driver.get(
    "https://scholar.google.com/scholar?start=0&hl=en&as_sdt=0%2C5&q=mountain+torrent&btnG="
)
#%%
a_s.driver.get(
    "https://scholar.google.com/scholar?start=0&hl=en&as_sdt=0%2C5&q=hydrological+monitoring&btnG="
)
#%%
a_s.driver.get(
    "https://scholar.google.com/scholar?start=0&hl=en&as_sdt=0%2C5&q=mountain+torrent&btnG="
)
# %%
# some examples for flooad ai
a_s.crawl("montain flood", 5, True)

# %%
a_s.crawl("hydrological monitoring", 5, True)

# %%
a_s.crawl("hydrological", 5, True)
# %%
a_s.crawl("meteorological precipitation", 5, True)
# %%
a_s.crawl("hydrological machine learning", 5, True)
# %%
a_s.crawl("meteorological big data", 5, True)
# %%
a_s.crawl("mountain torrents disaster monitor", 5, True)
# %%
a_s.crawl("mountain torrents disaster prevention", 5, True)
# %%
a_s.crawl("mountain torrents loss assessment", 5, True)
# %%
a_s.crawl("hydrological remote sensing", 5, True)
#%%
# some example for systemic risk
a_s.crawl("Macroprudential systemic risk measure machine learning", 5, False)

# %%
a_s.crawl("Macroprudential systemic risk measure statistics learning", 5, False)

# %%
a_s.crawl("Macroprudential systemic risk measure", 5, False)

# %%
a_s.crawl("Macroprudential systemic risk measure big data", 5, False)

# %%
a_s.crawl("Macroprudential systemic risk measure AI", 5, False)
# %%
a_s.crawl("Macroprudential systemic risk measure Artificial Intelligence", 5, False)
# %%
# test for the troberta
# trajectory representation learning
# upsupervised pre-training approach
# transfer learning with supervised finetuning
a_s.crawl("trajectory representation learning", 5, True)
# %%
