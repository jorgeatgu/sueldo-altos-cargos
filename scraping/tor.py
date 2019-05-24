# import requests


# session = requests.session()
# session.proxies = {}
# headers = {}
# headers['User-agent'] = "HotJava/1.1.2 FCS"
# session.proxies['http'] = 'socks5h://localhost:9050'
# session.proxies['https'] = 'socks5h://localhost:9050'
# r = session.get('http://httpbin.org/cookies')
# print(r.text)


import requests
url = 'https://httpbin.org/ip'
proxies = {
    "http": 'socks5h://localhost:9050',
    "https": 'socks5h://localhost:9050'
}
response = requests.get(url,proxies=proxies)
print(response.json())
