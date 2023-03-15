import requests
import os

TOKEN = 'токен'
FILE_PATH = ''
FILE_NAME = os.path.basename(FILE_PATH)
DISK_PATH = '/' + FILE_NAME  # путь, по которому будет сохранен файл на Диске

url_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

# получаем ссылку для загрузки файла на Диск
headers = {'Authorization': f'OAuth {TOKEN}'}
params = {'path': DISK_PATH, 'overwrite': 'true'}
response = requests.get(url_upload, headers=headers, params=params)
upload_url = response.json()['href']

# загружаем файл на Диск
with open(FILE_PATH, 'rb') as f:
    response = requests.put(upload_url, headers=headers, files={'file': f})

if response.status_code == 201:
    print(f'Файл "{FILE_NAME}" успешно загружен на Диск в папку "{DISK_PATH}"')
else:
    print(f'Ошибка загрузки файла на Диск: {response.text}')