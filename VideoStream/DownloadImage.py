import requests 

url = 'https://focus4software.com/TestCard.jpg'

r = requests.get(url) 

with open('TestCard.jpg', 'wb') as f:
    f.write(r.content)