import requests

BASE_URL = "https://stellarburgers.education-services.ru/api"

class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL

    def post(self, endpoint, data=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers)

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=headers)
    
    def delete(self, endpoint, headers=None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
