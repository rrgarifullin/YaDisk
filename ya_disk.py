import requests
import os


class YaUpload:
    def __init__(self, file_path):
        self.file_path = file_path

    def upload(self):
        url_get = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers_get = {
             'Accept': 'application/json',
             'Authorization': ''
        }
        params_get = {
            'path': os.path.basename(self.file_path)
        }
        response_get = requests.get(url_get, headers=headers_get, params=params_get)

        url_put = response_get.json()['href']
        with open(os.path.abspath(self.file_path), 'rb') as f:
            response_put = requests.put(url_put, files={'file': f})
        return response_put


file = input('Введите путь до файла: ')
uploader = YaUpload(file)
result = uploader.upload()
if result.status_code == 201:
    print('Файл успешно загружен')
elif result.status_code == 202:
    print('Ожидает загрузки')
else:
    print(result)