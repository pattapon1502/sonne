#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
'''
import json, requests

url = 'http://sigma.cpe.kmutt.ac.th:3000/lexto'
context = "none"
doll_series = "prototypes001"

while(True):

    input = raw_input()
    
    data = {"sentence": input, "context": context, "doll_series": doll_series}
    res = requests.post(url=url, data=data)

    print res.json()['sentence'] + " " + res.json()['context']
    
    context = res.json()['context']
'''

def isthere2(text, data):

    for i in range(len(text)):
        
        if(i+len(data) <= len(text)):
            
            if(text[i:i+len(data)] == data[0:len(data)]):
                
                return True

    return False


if __name__ == "__main__":

        
    text = sys.argv[1].split()
    test = sys.argv[2].split()
    print text
    
    print isthere2(text, test)
