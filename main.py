import requests
from pprint import pprint

with open ("file_token", "r") as file_token:
    token = file_token.read().strip()

# token = input("Введите токен = ")

# owner_id = input("Введите ID = ")
url = 'https://api.vk.com/method/photos.get'
params = {
    "owner_id": "448286812",
    'access_token': token,
    'album_id': "profile",
    "photo_sizes": '1',
    'v': "5.131",
    'extended': '1',
    "count": '100'
}

respond = requests.get(url, params=params)
# pprint(respond.json())
for Foto_big_size in respond.json()["response"]['items']:
    print("имя данной фотки будет: ", str(Foto_big_size["likes"]['count']) + "/" + str(Foto_big_size["date"]), ", a ee url:",Foto_big_size["sizes"][-1]['url'])
    print("_________________________________________________")


# pprint(respond.json())



