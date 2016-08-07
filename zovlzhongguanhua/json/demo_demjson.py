# -*- coding: UTF-8 -*-


import demjson


def demjson_encode():
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    json = demjson.encode(data)
    print json


def demjson_decode():
    json = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
    text = demjson.decode(json)
    print text


# demjson_encode()
demjson_decode()