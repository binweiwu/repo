#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2014-7-11

@author: Kenbin
'''
import collections
# regular unsorteddictionary
d = {'banana':3.1, 'apple':4.222, 'pear':3.12, 'orange':3.12}
print d
# dictionary sorted by key
sort_by_key = collections.OrderedDict(sorted(d.items(), key = lambda t: t[0]))
print sort_by_key
print type(sort_by_key)
print dir(sort_by_key)
# dictionary sorted by value
sort_by_value = collections.OrderedDict(sorted(d.items(), key = lambda t: t[1]))
print sort_by_value

# dictionary sorted by length of the key string
sort_by_keylength = collections.OrderedDict(sorted(d.items(), key = lambda t: len(t[0])))
print sort_by_keylength

# dictionary sorted by length of the value string
# sort_by_valuelength = collections.OrderedDict(sorted(d.items(), key = lambda t: len(str(t[1]))))
# print sort_by_keylength













