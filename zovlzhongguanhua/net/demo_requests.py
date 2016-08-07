# -*- coding: UTF-8 -*-


import requests
from PIL import Image
from io import StringIO
import json


def get_text():
    print '-----------------------------------------------------------------------------'
    url = 'https://api.github.com/events'
    r = requests.get(url)
    print_response(r)


def post_text():
    print '-----------------------------------------------------------------------------'
    url = 'http://httpbin.org/post'
    data = {'key': 'value'}
    r = requests.post(url, data)
    print_response(r)

    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    r = requests.post(url, data=json.dumps(payload))
    print_response(r)


def post_files():
    print '-----------------------------------------------------------------------------'
    url = 'http://httpbin.org/post'
    files = {'file': open('file.txt', 'rb')}
    r = requests.post(url, files)
    print_response(r)


def print_response(r):
    print '-----------------------------------------------------------------------------'
    print 'status_code: ' + str(r.status_code)
    print 'text: ' + str(r.text)
    print 'content: ' + str(r.content)
    print 'json: ' + str(r.json())
    print 'headers: ' + str(r.headers)
    print 'apparent_encoding: ' + str(r.apparent_encoding)
    print 'cookies: ' + str(r.cookies)
    print 'elapsed: ' + str(r.elapsed)
    print 'encoding: ' + str(r.encoding)
    print 'history: ' + str(r.history)
    print 'is_permanent_redirect: ' + str(r.is_permanent_redirect)
    print 'is_redirect: ' + str(r.is_redirect)
    print 'links: ' + str(r.links)
    print 'ok: ' + str(r.ok)
    print 'raise_for_status: ' + str(r.raise_for_status())


def get_image():
    r = requests.get(url='http://scimg.jb51.net/allimg/160618/77-16061Q44U6444.jpg')
    show_response(r)


def show_response(r):
    buffer = r.content
    fp = StringIO(buffer)
    i = Image.open(fp)





print dir(requests)
print globals()
print locals()



post_text()
# post_files()

