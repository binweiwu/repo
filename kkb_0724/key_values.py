#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
created on 2014-7-24
@author£ºkkb
'''
def kv():
    a = {'k11':'Imak11','k21':'iamk21'}
    print a.items()
    for key, value in a.items():
        print key, '-', value

kv()
