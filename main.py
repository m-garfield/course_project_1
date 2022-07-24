import requests
import yadisk
from pprint import pprint

with open ("file_token", "r") as file_token:
    token = file_token.read().strip()

# token = input("Введите токен = ")

# owner_id = input("Введите ID = ")
url = 'https://api.vk.com/method/photos.get'
params = {
    "owner_id": "629727012",
    'access_token': token,
    'album_id': "profile",
    "photo_sizes": '1',
    'v': "5.131",
    'extended': '1',
    "count": '100'
}

respond = requests.get(url, params=params)
# pprint(respond.json())
with open("file_ya_token", "r") as file_ya_token:
    token_ya = file_ya_token.read()

y = yadisk.YaDisk(token=token_ya)
if y.check_token():
    if not y.is_dir("/Dir_of_Foto"):
        y.mkdir("/Dir_of_Foto")
        print('Папка "/Dir_of_Foto" создана, загружаем фото')
    else:
        print("Папка существует, загружаем фото ")
for foto_big_size in respond.json()["response"]['items']:
    name_foto = str(foto_big_size["likes"]['count']) + "/" + str(foto_big_size["date"])
    url_foto = foto_big_size["sizes"][-1]['url']

    # print("имя данной фотки будет: ", str(Foto_big_size["likes"]['count']) + "/" + str(Foto_big_size["date"]), ", a ee url:",Foto_big_size["sizes"][-1]['url'])


    y.download("/Dir_of_Foto"+ name_foto, url_foto)

# вторая  часть , отправляем  фотку на яндекс диск

# токен     AQAAAABQRXTlAAhDhQfNmGSPcUUeiWPRpyPWFhM






