import socks
import socket
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#set socks5 proxy to use tor

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket
req = Request('http://check.torproject.org', headers={'User-Agent': 'Mozilla/5.0', })
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
print(soup('title')[0].get_text())
