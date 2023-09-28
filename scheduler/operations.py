import requests
import json


BASE_URL = 'http://127.0.0.1:8000/'

HEADERS = {
    'Content-Type': 'application/json'
}

class Operations:


    @staticmethod
    def post(endpoint, data):

        url = BASE_URL + endpoint
        data = json.dumps(data)
        response = requests.post(url=url, data=data, headers=HEADERS)

        return response.status_code
    
    @staticmethod
    def get(endpoint):

        url = BASE_URL + endpoint
        response = requests.get(url=url, headers=HEADERS)
        data = response.json()

        return data, response.status_code
    
    @staticmethod
    def delete(endpoint):

        url = BASE_URL + endpoint
        response = requests.delete(url=url, headers=HEADERS)

        return response.status_code
    
    @staticmethod
    def put(endpoint, data):

        url = BASE_URL + endpoint
        data = json.dumps(data)
        response = requests.put(url=url, data=data, headers=HEADERS)
        data = response.json

        return data, response.status_code
    
