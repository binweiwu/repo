# coding: utf-8
'''
Created on 2014-7-18
#  dict 和  OrderedDict的区别
@author: Kenbin
'''
import collections

# print 'Regular dictionary:'
# kkb = {}
# kkb['excel'] = 'A'
# kkb['ppt'] = 'B'
# kkb['word'] = 'C'
# 
# for k,v in kkb.items():
#     print k,v
#     
# print '\nOrderedDict:' #OrderedDict是dict的子类，它记住了内容添加的顺序。
# kkb = collections.OrderedDict()
# kkb['excel'] = 'A'
# kkb['ppt'] = 'B'
# kkb['word'] = 'C'
# for k,v in kkb.items():
#     print k,v

# OrderedDict要内容和顺序完全相同才会视为相等
print"dict: "
kkb = {}
kkb['excel'] = 'A'
kkb['ppt'] = 'B'
kkb['word'] = 'C'

kkb1 = {}
kkb1['word'] = 'C'
kkb1['excel'] = 'A'
kkb1['ppt'] = 'B'
print kkb == kkb1

print "OrdreedDict:"
kkb = collections.OrderedDict()
kkb['excel'] = 'A'
kkb['ppt'] = 'B'
kkb['word'] = 'C'

kkb1 = collections.OrderedDict()
kkb1['word'] = 'C'
kkb1['excel'] = 'A'
kkb1['ppt'] = 'B'
print kkb == kkb1
# print __doc__