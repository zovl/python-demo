# -*- coding: UTF-8 -*-


import httplib2
import urllib


def get_text():
    print '-----------------------------------------------------------------------------'
    h = httplib2.Http(".cache")
    url = "http://example.org/"
    method = "GET"
    resp, content = h.request(url, method)
    print resp
    print content


def put_text():
    print '-----------------------------------------------------------------------------'
    h = httplib2.Http(".cache")
    h.add_credentials('name', 'password')

    method = "PUT"
    url = "https://example.org/chap/2"
    body = "This is text"
    headers = {'content-type': 'text/plain'}

    resp, content = h.request(url, method, body=body, headers=headers)
    print resp
    print content

    print '-----------------------------------------------------------------------------'

    headers = {'cache-control': 'no-cache'}

    resp, content = h.request(url, method, body=body, headers=headers)
    print resp
    print content


def post_text():
    print '-----------------------------------------------------------------------------'
    h = httplib2.Http(".cache")
    data = dict(name="Joe", comment="A test comment")
    url = "http://bitworking.org/news/223/Meet-Ares"
    method = "POST"
    resp, content = h.request(url, method, body=urllib.urlencode(data))
    print resp
    print content


def post_text_2():
    h = httplib2.Http(".cache")
    method = "POST"
    url = 'http://www.example.com/login'
    body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    method = 'POST'
    resp, content = h.request(url, method, headers=headers, body=urllib.urlencode(body))
    print resp
    print content

    print '-----------------------------------------------------------------------------'

    headers = {'Cookie': resp['set-cookie']}
    url = 'http://www.example.com/home'
    method = 'GET'
    response, content = h.request(url, method, headers=headers)
    print resp
    print content


print dir(httplib2)
print globals()
print locals()



# get_text()
# put_text()
# post_text()
# post_text_2()