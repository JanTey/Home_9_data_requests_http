import requests

# установка токена
token = '2619421814940190'

# создание списка супергероев
superheroes = ['Hulk', 'Captain America', 'Thanos']

# создание словаря для хранения id и показателей интеллекта
intelligence = {}

# цикл для поиска id и показателей интеллекта каждого супергероя
for hero in superheroes:
    # запрос id супергероя
    url_search = f'https://superheroapi.com/api/{token}/search/{hero}'
    response_search = requests.get(url_search)
    hero_id = response_search.json()['results'][0]['id']
    
    # запрос показателя интеллекта супергероя
    url_powerstats = f'https://superheroapi.com/api/{token}/{hero_id}/powerstats'
    response_powerstats = requests.get(url_powerstats)
    intelligence[hero] = int(response_powerstats.json()['intelligence'])

# вывод самого умного супергероя
smartest_hero = max(intelligence, key=intelligence.get)
print(f'{smartest_hero} самый умный супергерой со значением интеллекта {intelligence[smartest_hero]}.')