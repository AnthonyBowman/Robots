import requests 

img = open('image.jpg', 'rb')
requests.post('http://192.168.1.101:5000/video_feed', data=img)