# Crypto Risk Management with Buying and Selling

Javascript (React, Recharts) implementation of analysis described by Benjamin Cowen:

[Ethereum: Risk management with buying and selling](https://www.youtube.com/watch?v=OvktrLJlwDA&app=desktop)
[Bitcoin: Risk management with buying and selling](https://www.youtube.com/watch?v=FznCM6rYki0)

## Downloading data

Download historical data:

- https://finance.yahoo.com/quote/BTC-USD/history
- https://etherscan.io/chart/etherprice

Convert CSV to JS:

    curl -L https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1410912000&period2=1622678400&interval=1d&events=history&includeAdjustedClose=true > btc-usd.csv
    ./csv2js.py btc-usd.csv src/bitcoin-data.js

## How to run the code

    npm install
    npm start

Open [http://localhost:3000/](http://localhost:3000/) in your browser.

![screenshot](https://raw.githubusercontent.com/sdrpa/crypto-risk-management/master/screenshot.png)

## Other indicators

- [Power Law Oscillator](https://stats.buybitcoinworldwide.com/power-law-oscillator/)
- [Fear and Greed index](https://alternative.me/crypto/fear-and-greed-index/)
