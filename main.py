import json
import requests
import yadisk


import time
from tqdm import tqdm



json_dic = []
with open("file_token", "r") as file_token:
    token = file_token.read().strip()
token_ya = input("Введите токен с Yandex полигона: ")
owner_id = input("Введите ID: ")
count = 5
count = input("Введите желаемое количество загружаемых фото: ")
url = 'https://api.vk.com/method/photos.get'
params = {
    "owner_id": owner_id,
    'access_token': token,
    'album_id': "profile",
    "photo_sizes": '1',
    'v': "5.131",
    'extended': '1',
    "count": count
}
respond = requests.get(url, params=params)
y = yadisk.YaDisk(token=token_ya)
if y.check_token():
    if not y.is_dir("/Dir_of_Foto"):
        y.mkdir("/Dir_of_Foto")
for i in tqdm(range(int(count))):
    for foto_big_size in respond.json()['response']['items']:
        name_foto = "/Dir_of_Foto/" + str(foto_big_size["likes"]['count']) + "_" + str(foto_big_size["date"])
        url_foto = foto_big_size["sizes"][-1]['url']
        y.upload_url(url_foto, name_foto)
        json_dic.append({"file_name": str(foto_big_size["likes"]['count']) + '.jpg', "size": str(foto_big_size["sizes"][-1]['type'])})
        with open("file_json", "w") as file_json:
            json.dump(json_dic, file_json)

# токен     AQAAAABQRXTlAAhDhQfNmGSPcUUeiWPRpyPWFhM






