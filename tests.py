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
    c = Converter(baseCurrency='USD')
    latestRates = c.getLatestRates()
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
        assert False, "The base rate isn't USD."
    if 'rates' in latestRates:
        assert True
    else:
        assert False, "The exchange rates are missing."

def testHistoricalRates():
    c = Converter(queryDate='2017-01-01')
    historicalRates = c.getHistoricalRates()
    if historicalRates:
        assert True
    else:
        assert False, "Historical forex rates not retrieved."
    if 'date' in historicalRates:
        assert True
    else:
        assert False, "The date is missing."
    if historicalRates['base'] == 'EUR':
        assert True
    else:
        assert False, "The base rate is not EUR."
    if 'rates' in historicalRates:
        assert True
    else:
        assert False, "The exchange rates are missing."

def testHistoricalRatesWithBase():
    c = Converter(queryDate='2017-01-01', baseCurrency='USD')
    historicalRates = c.getHistoricalRates()
    if historicalRates:
        assert True
    else:
        assert False, "Historical forex rates not retrieved."
    if 'date' in historicalRates:
        assert True
    else:
        assert False, "The date is missing."
    if historicalRates['base'] == 'USD':
        assert True
    else:
        assert False, "The base rate isn't USD."
    if 'rates' in historicalRates:
        assert True
    else:
        assert False, "The exchange rates are missing."