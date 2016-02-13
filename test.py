#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import json, requests


url = 'http://sigma.cpe.kmutt.ac.th:3000/project'
context = "none"
doll_series = "prototypes001"

while(True):

    input = raw_input()
    
    data = {"sentence": input, "context": context, "doll_series": doll_series}
    res = requests.post(url=url, data=data)

    print res.json()['sentence'] + " " + res.json()['context'] + " " +res.json()['action'] + " " + res.json()['sound']
    
    context = res.json()['context']

while(True):

    input = raw_input()
    for i in range(len(action)):
    
        if(input == action[i]):
        
            print i
    
