import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = ''.join(text.split())

    return text

def extract_intent(text):
    entities = {
        'crypto': None,
        'fial': None
    }

    crypto_keywords = {'bitcoin': 'BTC', 'ethereum': 'ETH', 'litecoin': 'LTC'}
    fiat_keywords = {'usd': 'USD', 'eur': 'EUR', 'gbp': 'GBP'}

    words = text.lower().split()

    for word in words:
        if word in crypto_keywords:
            entities['crypto'] = crypto_keywords[word]
        elif word in fiat_keywords:
            entities['fiat'] = fiat_keywords[word]

    return entities