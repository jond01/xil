import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


POALIM_URL = "https://www.bankhapoalim.co.il/he/foreign-currency/exchange-rates"
TABLE_ID = "fer-table-content"

driver = webdriver.Chrome()
driver.get(POALIM_URL)
elem = driver.find_element(By.ID, TABLE_ID)
table_html = elem.get_attribute("innerHTML")
driver.close()

dfs = pd.read_html(table_html, header=0, skiprows=1, index_col=0)
assert len(dfs) == 1
df = dfs[0]
print(df)
