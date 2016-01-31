#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime
import dateparser
import sympy
import random
import json

def isthere(text, word):

    for i in range(len(text)):
        if(text[i] == word):
            return True;

    return False;

def date(date):

    output = getweekday(date) + "ที่" + str(date.day) + getmonth(date, 0) + "ปี พ.ศ." + str(date.year + 543)
    return output
	
def getweekday(date):

    temp = date.weekday()
    
    if(temp == 0):
        return "วันจันทร์"
    elif(temp == 1):
        return "วันอังคาร"
    elif(temp == 2):
        return "วันพุธ"
    elif(temp == 3):
        return "วันพฤหัสบดี"
    elif(temp == 4):
        return "วันศุกร์"
    elif(temp == 5):
        return "วันเสาร์"
    elif(temp == 6):
        return "วันอาทิตย์"
    else:
        return "none"

def getmonth(date, delta):

    temp = (date.month + delta) % 12

    if(temp == 1):
        return "เดือนมกราคม "
    elif(temp == 2):
        return "เดือนกุมภาพันธ์ "
    elif(temp == 3):
        return "เดือนมีนาคม "
    elif(temp == 4):
        return "เดือนเมษายน "
    elif(temp == 5):
        return "เดือนพฤษภาคม "
    elif(temp == 6):
        return "เดือนมิถุนายน "
    elif(temp == 7):
        return "เดือนกรกฏาคม "
    elif(temp == 8):
        return "เดือนสิงหาคม "
    elif(temp == 9):
        return "เดือนกันยายน "
    elif(temp == 10):
        return "เดือนตุลาคม "
    elif(temp == 11):
        return "เดือนพฤศจิกายน "
    elif(temp == 12 or temp == 0):
        return "เดือนธันวาคม "
    else:	
        return "none"
	
def calculate(text):

    question = ""

    for i in range(len(text)):
        if(text[i] ==  "เท่ากับ"):
            return sympy.sympify(question)

        if(text[i] ==  "บวก" or text[i] == "+"):
            question = question + "+"
        elif(text[i] == "ลบ" or text[i] == "-"):
            question = question + "-" 
        elif(text[i] == "คูณ" or text[i] == "x"):
            question = question + "*"
        elif(text[i] == "หาร" or text[i] == "/"):
            question = question + "/"
        elif(text[i] == "ยกกำลัง"):
            question = question + "**"
        else:
            question = question + text[i]
    #print question
    return sympy.sympify(question)
            

def main(text, context):
    
    for i in range(len(text)):
        if(i+1 < len(text) and text[i] == "วัน" and text[i+1] == "อะไร"):

            if(isthere(text, "เมื่อวาน")):
                return [date(datetime.datetime.now() + datetime.timedelta(days=-1))]
            elif(isthere(text, "พรุ่งนี้")):
                return [date(datetime.datetime.now() + datetime.timedelta(days=1))]
            elif(isthere(text, "มะรืน")):
                return [date(datetime.datetime.now() + datetime.timedelta(days=2))]
            elif(isthere(text, "เมื่อวานซืน")):
                return [date(datetime.datetime.now() + datetime.timedelta(days=-2))]
            else:
                return [date(datetime.datetime.now())]

        if(i+1 < len(text) and text[i] == "เดือน" and text[i+1] == "อะไร"):
            if(isthere(text, "หน้า")):
                return [getmonth(datetime.datetime.now(), 1)]
            elif(isthere(text, "ที่แล้ว")):
                return [getmonth(datetime.datetime.now(), -1)]
            else:
                return [getmonth(datetime.datetime.now(), 0)]
                
                
        if(i+1 < len(text) and text[i] == "เล่น" and text[i+1] == "เกม" or (text[i] == "เล่น" and len(text) == 1)):
            return game(text, context)

    return ["ไม่รู้อ่ะ"]
    
def game(text, context):

    if(context[0] == "none"):
        return ["เล่นเกมอะไร", "เกม"]

    if(len(context) > 1 and context[1] == "เกมเสียงอะไร"):
        return playgame("เกมเสียงอะไร", text, context)
        
    elif(len(context) > 1 and context[1] == "เกมบวกลบเลข"):
        return playgame("เกมบวกลบเลข", text, context)
        
    elif(len(context) > 1 and context[1] == "เกมอะไรต่างจากพวก"):
        return playgame("เกมอะไรต่างจากพวก", text, context)
        
    else:
    
        for i in range(len(text)):

            if(i+2 < len(text) and text[i] == "เกม" and text[i+1] == "เสียง" and text[i+2] == "อะไร"):
                return ["เล่นเกมเสียงอะไร พร้อมไหม", "เกม เกมเสียงอะไร พร้อมไหม"]
                
            elif(i+3 < len(text) and text[i] == "เกม" and text[i+1] == "บวก" and text[i+2] == "ลบ" and text[i+3] == "เลข"):
                return ["เล่นเกมบวกลบเลข พร้อมไหม", "เกม เกมบวกลบเลข พร้อมไหม"]
    
            elif(i+4 < len(text) and text[i] == "เกม" and text[i+1] == "อะไร" and text[i+2] == "ต่าง" and text[i+3] == "จาก" and text[i+4] == "พวก"):
                return ["เล่นเกมอะไรต่างจากพวก พร้อมไหม", "เกม เกมอะไรต่างจากพวก พร้อมไหม"]
    return [" "]
    


def playgame(game, text, context):

    #start
    if(context[2] == "พร้อมไหม" or context[2] == "เล่นอีกไหม"):
    
        for i in range(len(text)):
        
            if(text[i] == "พร้อม" or (i+1 < len(text) and text[i] == "เอา" and text[i-1] == "เลย") or text[i] == "เล่น"):
            
                if(game == "เกมเสียงอะไร"):
                    ques, ans = game001()
                elif(game == "เกมบวกลบเลข"):
                    ques, ans = game002()
                elif(game == "เกมอะไรต่างจากพวก"):
                    ques, ans = game003()
                else:
                    ques, ans = [" ", " "]
                return [ques, "เกม " + game + " " + ques + " " + ans]
                
        else: # quit
            return ["ไม่เล่นแล้วเหรอ"]
    # answer            
    else:
        
        for i in range(len(text)):

            if(len(context) > 2 and text[i] == context[3]):
                return ["ถูกต้อง เล่นอีกไหม", "เกม " +game+ " เล่นอีกไหม"]
                
            elif(isthere(text, "เปลี่ยน")):
            
                if(game == "เกมเสียงอะไร"):
                    ques, ans = game001()
                elif(game == "เกมบวกลบเลข"):
                    ques, ans = game002()
                elif(game == "เกมอะไรต่างจากพวก"):
                    ques, ans = game003()
                else:
                    ques, ans = [" ", " "]
                    
                return [ques, "เกม " + game + " " + ques + " " + ans]
                
            elif((i+1 < len(text) and text[i] == "ฟัง" and text[i+1] == "ใหม่") or (i+1 < len(text) and text[i] == "ขอ" and text[i+1] == "อีก")):
                return [context[2], "เกม " + game + " "+ context[2] + " " + context[3]]
                
            elif(text[i] == "ยอมแพ้" or text[i] == "เฉลย"):  
                return ["คำตอบคือ "+context[3]+ " เล่นอีกไหม", "เกม " + game + " เล่นอีกไหม"]
                
            elif(isthere(text, "ไม่")):
                return ["ไม่เล่นแล้วเหรอ"]
            
            else:
                return ["ผิด", "เกม " + game + " " + context[2] + " " + context[3]]
        
    return [" "]
        
            
def game001():
         
    with open('game/game001.json') as data_file:    
        data = json.load(data_file)

    ran = random.randrange(1, data[0]['number']+1)
    return [data[ran]['sound_path'].encode('utf-8'), data[ran]['answer'].encode('utf-8')]

def game002():
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    if(random.randrange(0, 2) == 1):
        oper = "+"
    else:
        oper = "-"
        
    if(num1 > num2):
        ques = str(num1)+oper+str(+num2)
    else:
        ques = str(num2)+oper+str(num1)
    
    ans = str(sympy.sympify(ques))
    return [ques, ans]

def game003():

    with open('game/game003.json') as data_file:    
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
    
    return [ques, ans]

if __name__ == "__main__":

    if(len(sys.argv) < 3):
        sys.exit()
        
    text = sys.argv[1].split()
    context = sys.argv[2].split()
    
    if(isthere(context, "เกม")):
        output = game(text, context)
    else:
        output = main(text, context)
        
    if(len(output) == 1):
        print output[0]
        #a = output[0].encode('utf-8')
        #print a
        print "none"
    else:
        print output[0]
        print output[1]
    



