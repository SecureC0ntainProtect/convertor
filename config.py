import os


BOT_TOKEN = os.getenv('BOT_TOKEN', None)

# https://min-api.cryptocompare.com/pricing
# Choose a free key for the test
CRYPTOCOMPARE_API_KEY = os.getenv('CRYPTOCOMPARE_API_KEY', None)

currencies = {
    'доллар': 'USD',
    'фунт': 'GBP',
    'евро': 'EUR',
    'рубль': 'RUB',
    'биткоин': 'BTC',
    'эфириум': 'ETC'
}
