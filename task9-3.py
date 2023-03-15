import requests
import datetime

SITE = 'stackoverflow'  # сайт, для которого ищем вопросы
TAG = 'python'  # тэг, который должен содержаться в вопросе
DAYS = 2  # период в днях, за который ищем вопросы

url = f'https://api.stackexchange.com/2.3/questions'
params = {'fromdate': int((datetime.datetime.now() - datetime.timedelta(days=DAYS)).timestamp()),
          'todate': int(datetime.datetime.now().timestamp()),
          'order': 'desc',
          'sort': 'creation',
          'tagged': TAG,
          'site': SITE}

response = requests.get(url, params=params)

if response.status_code == 200:
    questions = response.json()['items']
    for question in questions:
        print(f"Заголовок: {question['title']}\nСсылка: {question['link']}\n")
else:
    print(f"Ошибка получения списка вопросов: {response.text}")