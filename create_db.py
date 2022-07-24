#%%
import sqlite3

data_base_name = "knowledge_distillation"
conn = sqlite3.connect(f"data/{data_base_name}.db")
c = conn.cursor()
#%%
c.execute(
    """CREATE TABLE PAPER (
    TITLE CHAR(100) NOT NULL,
    AUTHOR CHAR(50) NOT NULL,
    QUERY CHAR(40) NOT NULL,
    CITE_NUM CHAR(40),
    ABSTRACT CHAR(300) NOT NULL,
    MAIN_HERF CHAR(100) NOT NULL,
    PDF_HERF CHAR(100),
    BIBTEX CHAR(300));"""
)

# %%
conn.commit()
conn.close()
# %%