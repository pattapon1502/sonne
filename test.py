#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import json

with open('game003.json') as data_file:    
    data = json.load(data_file)

rantype1 = random.randrange(1, data[0]['number']+1)
rantype2 = random.randrange(1, data[0]['number']+1)
while(rantype1 == rantype2):
    rantype2 = random.randrange(1, data[0]['number']+1)

print rantype1
print rantype2
print data[1]['number']
ranthing1 = random.randrange(0, data[rantype1]['number'])
ranthing2 = random.randrange(0, data[rantype1]['number'])
while(ranthing1 == ranthing2):
    ranthing2 = random.randrange(0, data[rantype1]['number'])
ranthing3 = random.randrange(0, data[rantype2]['number'])

x = [data[rantype1]['name'][ranthing1].encode('utf-8'), data[rantype1]['name'][ranthing2].encode('utf-8'), data[rantype2]['name'][ranthing3].encode('utf-8')]
random.shuffle(x)
ques = x[0] + " " + x[1] + " " + x[2]
ans = data[rantype2]['name'][ranthing3].encode('utf-8')
print x
print ques
print ans