#!/usr/bin/env python

import requests
print(requests.__version__)

r = requests.get(‘https://raw.githubusercontent.com/leevtori/404-lab1/master/main.py')
#print(r)
#print(dir(r))
print(r.text)
print(r.status_code)
