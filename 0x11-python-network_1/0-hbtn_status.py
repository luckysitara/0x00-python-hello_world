#!/usr/bin/python3
"""
This is the Script that fetches https://alx-intranet.hbtn.io/status written by bughacker
"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

re = with urllib.request.urlopen(url):
    status_page = re.read()
    print('Body response:')
    print('\t- type: {}'.format(type(status_page)))
    print('\t- content: {}'.format(status_page))
    print('\t- utf8 content: {}'.format(status_page.decode('utf-8')))

