import requests as r
import collections

# Define a Converter as a base class.

class Converter:

    baseCurrency = None
    targetCurrency = None
    queryDate = None

    currentRates = None
    historicalRates = None

    def __init__(self, baseCurrency=None, targetCurrency=None, queryDate=None):
        self.baseCurrency = baseCurrency
        self.targetCurrency = targetCurrency
        self.queryDate = queryDate

    def getLatestRates(self):
        if self.baseCurrency:
            self.currentRates = r.get('http://api.fixer.io/latest?base=' + self.baseCurrency).json()
        else:
            self.currentRates = r.get('http://api.fixer.io/latest').json()
        return self.currentRates
    
    def getHistoricalRates(self):
        if self.baseCurrency:
            self.historicalRates = r.get('http://api.fixer.io/' + self.queryDate + '?base=' + self.baseCurrency).json()
        else:
            self.historicalRates = r.get('http://api.fixer.io/' + self.queryDate).json()
        return self.historicalRates

