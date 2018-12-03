# test pyquery

import requests
from pyquery import PyQuery as pq

url = 'http://qqsh.gamebbs.qq.com/forum.php'
rsp = requests.get(url)

doc = pq(rsp.text)
items = doc('.fl_tb td h2 a').items()
for a in items:
    print(a.text())
