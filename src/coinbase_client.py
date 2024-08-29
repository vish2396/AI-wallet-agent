import requests

class CoinbaseClient:
    def _init_(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://api.coinbase.com/v2/'

    def get_price(self, crypto_currency):
        endpoint = f'prices/{crypto_currency}-USD/spot'
        response = requests.get(self.base_url + endpoint)
        if response.status_code == 200:
            data = response.json()
            return data['data']['amount']
        else:
            return None