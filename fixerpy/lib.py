import requests as r
import collections

# Define a Converter as a base class.

class Converter:

    baseCurrency = None
    targetCurrency = None
    queryDate = None

    def getLatestRates(self, baseCurrency=None):
        if baseCurrency:
            self.baseCurrency = baseCurrency
            currentRates = r.get('http://api.fixer.io/latest?base=' + baseCurrency).json()
        else:
            currentRates = r.get('http://api.fixer.io/latest').json()
        return currentRates
    
    def getHistoricalRates(self, date, baseCurrency=None):
        if baseCurrency:
            self.baseCurrency = baseCurrency
            historicalRates = r.get('http://api.fixer.io/' + date + '?base=' + baseCurrency).json()
        else:
            historicalRates = r.get('http://api.fixer.io/' + date).json()
        return historicalRates

