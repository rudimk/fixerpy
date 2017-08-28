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
        assert False, "The base rate isn't USD."
    if 'rates' in latestRates:
        assert True
    else:
        assert False, "The exchange rates are missing."

def testHistoricalRates():
    c = Converter()
    historicalRates = c.getHistoricalRates(date='2017-01-01')
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
    c = Converter()
    historicalRates = c.getHistoricalRates(date='2017-01-01', baseCurrency='USD')
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