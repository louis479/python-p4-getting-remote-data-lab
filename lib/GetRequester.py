import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        print(f"DEBUG: Returning type: {type(response.text)}")  # Should say <class 'str'>
        return response.text
        
    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
        