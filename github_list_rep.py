import requests
import json

def get_rep(url: str):
    response = requests.get(url)
    return response.json()

username = input('Введите username: ')
url = 'https://api.github.com/users/'+username+'/repos'
response = get_rep(url)
rep = []
for itm in response:
    rep.append(itm['name'])
print(f'Список репозиториев пользователя {username}')
print(rep)
jsonString = json.dumps(rep)
jsonFile = open("data_rep.json", "w")
jsonFile.write(jsonString)
jsonFile.close()