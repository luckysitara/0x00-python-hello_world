#!/usr/bin/python3
'''
This is a Script that fetches https://intranet.hbtn.io/status written by precious(luckysitara, bughacker)
'''
from urllib import request

url = 'https://intranet.hbtn.io/status'
with request.urlopen(url) as response:
    the_page = response.read()
    print("""Body response:
    \t- type: {}'.format(type(the_page))
    \t- content: {}'.format(the_page))
    \t- utf8 content: {}'.format(the_page.decode('utf-8'))""")
