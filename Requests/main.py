import requests
from pprint import pprint

response = requests.get("http://google.com")
print(response)