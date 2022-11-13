"""
Mizrahi-Tefahot Bank scraper foreign exchange rates data:
https://www.mizrahi-tefahot.co.il/brokerage/foreignexchange/
Exchange calculator:
https://www.mizrahi-tefahot.co.il/brokerage/currancyexchange/
"""
import pandas as pd

_MIZRAHI_TEFAHOT_URL = "https://www.mizrahi-tefahot.co.il/brokerage/foreignexchange/"

df = pd.read_html(_MIZRAHI_TEFAHOT_URL, header=0)[0]
