from __future__ import absolute_import
from fixerpy import Converter

def testLatestRates():
    c = Converter()
    latestRates = c.getLatestRates()
    if latestRates:
        assert True
    else:
        assert False, "Current forex rates not retrieved."
    if 'date' in latestRates:
        assert True
    else:
        assert False, "The date is missing."
    if latestRates['base'] == 'EUR':
        assert True
    else:
        assert False, "The base rate is not EUR."
    if 'rates' in latestRates:
        assert True
    else:
        assert False, "The exchange rates are missing."

def testLatestRatesWithBase():
    c = Converter()
    latestRates = c.getLatestRates(baseCurrency='USD')
    if latestRates:
        assert True
    else:
        assert False, "Current forex rates not retrieved."
    if 'date' in latestRates:
        assert True
    else:
        assert False, "The date is missing."
    if latestRates['base'] == 'USD':
        assert True
    else:
        assert False, "The base rate is USD, overriding the default EUR."
    if 'rates' in latestRates:
        assert True
    else:
        assert False, "The exchange rates are missing."
