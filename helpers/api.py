import requests

class Api:
    BASE_URL = 'http://localhost:3000/api'

    def __init__(self, api_key):
        self.api_key = api_key

    def hooks(self):
        resp = requests.get(self.BASE_URL + '/hooks',
                            headers=self.build_headers())
        return resp.json()

    def profile(self):
        resp = requests.get(self.BASE_URL + '/profile',
                           headers=self.build_headers())
        return resp.json()

    def build_headers(self):
        return {
            'authorization': 'Bearer ' + self.api_key
        }
