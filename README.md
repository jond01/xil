# XIL

Gather and compare foreign currency exchange buy and sell rates offered by Israeli
banks.


## Banks data

The Bank of Israel [lists](https://www.boi.org.il/en/BankingSupervision/BanksAndBranchLocations/Pages/Default.aspx)
commercial Israeli banks. The XIL project supports the following banks:

| Bank and data source                                                                                                            | XIL module        | Tests | Bank name (Hebrew)           |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------|-------|------------------------------|
| [Bank Leumi Le-Israel](https://www.leumi.co.il/Lobby/currency_rates/40806/)                                                     | `leumi`           | :x:   | בנק לאומי לישראל             |
| [Bank Hapoalim](https://www.bankhapoalim.co.il/he/foreign-currency/exchange-rates)                                              | `poalim`          | :x:   | בנק הפועלים                  |
| [Mizrahi Tefahot Bank](https://www.mizrahi-tefahot.co.il/brokerage/currancyexchange/)                                           | `mizrahi_tefahot` | :x:   | בנק מזרחי טפחות              |
| [Israel Discount Bank](https://www.discountbank.co.il/DB/private/general-information/foreign-currency-transfers/exchange-rates) | `discount`        | :x:   | בנק דיסקונט לישראל           |
| [First International Bank of Israel](https://www.fibi.co.il/wps/portal/FibiMenu/Marketing/Private/ForeignCurrency/Trade/Rates)  | `fibi`            | :x:   | הבנק הבינלאומי הראשון לישראל |
| [Bank of Jerusalem](https://www.bankjerusalem.co.il/capital-market/rates)                                                       | `jerusalem`       | :x:   | בנק ירושלים                  |
| [Mercantile Discount Bank](https://www.mercantile.co.il/MB/private/foregin-currency/exchange-rate)                              | `mercantile`      | :x:   | בנק מרכנתיל דיסקונט          |
| [Bank Massad](https://www.bankmassad.co.il/wps/portal/FibiMenu/Marketing/Private/ForeignCurrency/ForexOnline/Rates)             | `massad`          | :x:   | בנק מסד                      |

For the data sources (websites and URLs) for each bank, see the docstring of the
corresponding XIL module.

Banks that are not supported yet:

- Bank Yahav (בנק יהב): no public information available.
  https://www.bank-yahav.co.il/investments/foreing-currency/
- One Zero Digital Bank (וואן זירו הבנק הדיגיטלי): no public information available.
  https://www.onezerobank.com/

## Installation
The project requires Python 3.10 or above. To install the project, run:
```shell
pip install git+https://github.com/jond01/xil.git
```

## Contributing to the XIL project
Please read the [Contribution Guide](CONTRIBUTING.md).
