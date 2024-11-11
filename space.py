#Før du kan bruke HTTP requests i Python må du laste ned Request biblioteket til Python.
#Dette gjør du ved å skrive pip install requests i terminalen, dette vil ikke være lastet ned med python.
import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print('The people currently in space are:')
for person in json['people']:
    print(person ['name'])