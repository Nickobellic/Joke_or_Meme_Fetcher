import random
from bs4 import BeautifulSoup
import requests

header = {
    'x-api-key': '4a13ea197dba4589af94d15c3b2a9e94'
}

cat_type = requests.get('https://humorapi.com/docs/#Joke-Categories', headers=header).content
soup = BeautifulSoup(cat_type, 'html.parser')
type = soup.select('ul[class="pageList"] li')
types = []
for i in type:
    types.append(i.text)
types = [i.lower() for i in types]

joke_or_meme = input('Joke or Meme: ')
search_or_random = input('search or random: ')
if joke_or_meme.upper() == "JOKE":
    if search_or_random.upper() == "SEARCH":
        MEME_ENDPOINT = "https://api.humorapi.com/jokes/search"
        param = {
            'min-rating': int(input('Enter the minimum rating: ')),
            'number': int(input("Enter the no.of Jokes: ")),
            'keywords': random.choice(types)
        }
        access = requests.get(url=MEME_ENDPOINT, headers=header, params=param).json()
        for i in range(len(access['jokes'])):
            joke = access['jokes'][i]['joke']
            print(joke)
    elif search_or_random.upper() == "RANDOM":
        MEME_ENDPOINT = "https://api.humorapi.com/jokes/random"
        parame = {
            'min-rating': int(input('Enter the minimum rating: ')),
        }
        access = requests.get(url=MEME_ENDPOINT, headers=header, params=parame).json()
        print(access['joke'])

    else:
        print('Try again')
elif joke_or_meme.upper() == "MEME":
    if search_or_random.upper() == "SEARCH":
        MEME_ENDPOINT = "https://api.humorapi.com/memes/search"
        param = {
            'keywords': random.choice(types),
            'min-rating': int(input('Enter the minimum rating: ')),
            'number': int(input("Enter the no.of Jokes: ")),
            'media-type': 'image'
        }
        access = requests.get(url=MEME_ENDPOINT, headers=header, params=param).json()
        for i in range(len(access['memes'])):
            meme = access['memes'][i]['url']
            print(f"MEME URLs: {meme}")
    elif search_or_random.upper() == "RANDOM":
        MEME_ENDPOINT = "https://api.humorapi.com/memes/random"
        param = {
            'min-rating': int(input('Enter the minimum rating: ')),
            'media-type': 'image'
        }
        access = requests.get(url=MEME_ENDPOINT, headers=header, params=param).json()
        print(f"MEME URL: {access['url']}")
    else:
        print('Try again')



