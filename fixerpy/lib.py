import requests as r
import collections

# Define a Converter as a base class.

class Converter:

    baseCurrency = None
    targetCurrency = None
    queryDate = None

    def getLatestRates(self):
        currentRates = r.get('http://api.fixer.io/latest').json()
        return currentRates


