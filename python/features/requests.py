import requests as rq

url = 'google.com'

try:
    resp = rq.get(url)
    print(resp)
