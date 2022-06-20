#%%
import sqlite3

conn = sqlite3.connect("data/troberta.db")
c = conn.cursor()
for row in c.execute("SELECT * FROM paper"):
    print(row)
# %%
db_names = ["TITLE", "AUTHOR", "QUERY", "CITE_NUM", "ABSTRACT", "MAIN_HREF","PDF_HREF", "BIBTEX"]
# TITLE CHAR(100) NOT NULL,
    # AUTHOR CHAR(50) NOT NULL,
    # QUERY CHAR(40) NOT NULL,
    # CITE_NUM CHAR(40),
    # ABSTRACT CHAR(300) NOT NULL,
    # MAIN_HERF CHAR(100) NOT NULL,
    # PDF_HERF CHAR(100),
    # BIBTEX CHAR(300));"""