import requests



class ApiClient:
    def __init__(self,base_url):
        self.base_url = base_url

    def post(self, endpoint, data=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers)

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=headers)
    
    def delete(self, endpoint, headers=None):
        return requests.delete(f"{self.base_url}{endpoint}", headers=headers)
