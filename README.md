# XIL

Gather and compare foreign currency exchange buy and sell rates offered by Israeli
banks.


## Banks data

The Bank of Israel [lists](https://www.boi.org.il/en/BankingSupervision/BanksAndBranchLocations/Pages/Default.aspx)
commercial Israeli banks. The XIL project supports the following banks:

| Bank                               | XIL module        | Tests | Bank name (Hebrew)           |
|------------------------------------|-------------------|-------|------------------------------|
| Bank Leumi Le-Israel               | `leumi`           | :x:   | בנק לאומי לישראל             |
| Bank Hapoalim                      | `poalim`          | :x:   | בנק הפועלים                  |
| Mizrahi Tefahot Bank               | `mizrahi_tefahot` | :x:   | בנק מזרחי טפחות              |
| Israel Discount Bank               | `discount`        | :x:   | בנק דיסקונט לישראל           |
| First International Bank of Israel | `fibi`            | :x:   | הבנק הבינלאומי הראשון לישראל |
| Bank of Jerusalem                  | `jerusalem`       | :x:   | בנק ירושלים                  |
| Union Bank of Israel               | `union`           | :x:   | בנק איגוד לישראל             |
| Mercantile Discount Bank           | `mercantile`      | :x:   | בנק מרכנתיל דיסקונט          |
| Bank Massad                        | `massad`          | :x:   | בנק מסד                      |

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
