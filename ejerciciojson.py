import json
import requests
from pprint import pprint

url = "https://raw.githubusercontent.com/arleserp/MinTIC2022/master/json/comprassmall.json" 

response = requests.get(url)
compras = json.loads(response.text)

pprint(compras)

