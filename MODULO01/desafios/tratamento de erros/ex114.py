import requests
try:
    url = 'https://www.youtube.com'
    if requests.get(url).status_code == 200:
        print('O site youtube está acessível no momento!')
except:
    print('O site youtube, não está acessível no momento!')
    