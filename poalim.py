import pandas as pd

POALIM_URL = "https://www.bankhapoalim.co.il/he/foreign-currency/exchange-rates"

df = pd.read_html(POALIM_URL)
print(f"{type(df) = }", df, sep="\n")
