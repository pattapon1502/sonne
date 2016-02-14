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
        
        if(i+len(word) <= len(text)):
            
            if(text[i:i+len(word)] == word[0:len(word)]):
                
                return True

    return False

def changenum(num):

    if(num == "ศูนย์"):
        return "0"
    elif(num == "หนึ่ง"):
        return "1"
    elif(num == "สอง"):
        return "2"
    elif(num == "สาม"):
        return "3"
    elif(num == "สี่"):
        return "4"
    elif(num == "ห้า"):
        return "5"
    elif(num == "หก"):
        return "6"
    elif(num == "เจ็ด"):
        return "7"
    elif(num == "แปด"):
        return "8"
    elif(num == "เก้า"):
        return "9"
    elif(num == "สิบ"):
        return "10"
    else:
        return ""

def calculate(text):

    ques = ""

    for i in range(len(text)):

        if(text[i] == "+" or text[i] == "บวก"):
            ques = ques + "+"
        elif(text[i] == "-" or text[i] == "ลบ"):
            ques = ques + "-"
        elif(text[i] == "x" or text[i] == "คูณ"):
            ques = ques + "*"
        elif(text[i] == "/" or text[i] == "หาร"):
            ques = ques + "/"
        else:
            try: 
                int(text[i])
                ques = ques + text[i]
            except ValueError:
                ques = ques + changenum(text[i])
    return ques

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

def getmonth(date):

    temp = date.month

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
	
    
    
def main(text, context):

    if(isthere(text, ["สวัสดี"]) or isthere(text, ["อรุณสวัสดิ์"]) or isthere(text, ["hello"])):
        '''if(datetime.datetime.now().hour > 6 and datetime.datetime.now().hour < 10):
            return ["สวัสดีตอนเช้า"]
        elif(datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 13):
            return ["สวัสดีตอนเที่ยง"]
        elif(datetime.datetime.now().hour >= 13 and datetime.datetime.now().hour < 16):
            return ["สวัสดีตอนบ่าย"]
        elif(datetime.datetime.now().hour >= 16 and datetime.datetime.now().hour < 18):
            return ["สวัสดีตอนเย็น"]
        else:'''
        return ["สวัสดี"]
    elif(isthere(text, ["บ๊ายบาย"]) or isthere(text, ["ลาก่อน"]) or isthere(text, ["ราตรีสวัสดิ์"]) or isthere(text, ["bye"])):
        if(datetime.datetime.now().hour >= 19):
            return ["ฝันดี", "none", "right_wave"]
        else:
            return ["บ๊ายบาย", "none", "right_wave"]
    elif(isthere(text, ["เล่น", "เกม"])):
        return game(text, context)
    elif(isthere(text, ["เล่านิทาน"]) or isthere(text, ["ฟัง", "นิทาน"])):
        return [""]

    # date and time
    elif(isthere(text, ["เดือน", "นี้", "เป็น", "เดือน", "อะไร"]) or isthere(text, ["เดือน", "นี้", "เดือน", "อะไร"])):
        return ["เดือนนี้เป็น" +getmonth(datetime.datetime.now())]
    elif(isthere(text, ["เดือน", "หน้าเป็น", "เดือน", "อะไร"]) or isthere(text, ["เดือน", "หน้า", "เดือน", "อะไร"])):
        return ["เดือนหน้าเป็น" +getmonth(datetime.datetime.now() + datetime.timedelta(days=30))]
    elif(isthere(text, ["เดือน", "ที่แล้ว", "เป็น", "เดือน", "อะไร"])or isthere(text, ["เดือน", "ที่แล้ว", "เดือน", "อะไร"])):
        return ["เดือนที่แล้วเป็น" +getmonth(datetime.datetime.now() + datetime.timedelta(days=-30))]

    elif(isthere(text, ["วันนี้", "เป็น", "วัน", "อะไร"]) or isthere(text, ["วันนี้", "วัน", "อะไร"])):
        return ["วันนี้เป็น" +getweekday(datetime.datetime.now())]
    elif(isthere(text, ["พรุ่งนี้", "เป็น", "วัน", "อะไร"]) or isthere(text, ["พรุ่งนี้", "วัน", "อะไร"])):
        return ["พรุ่งนี้เป็น" +getweekday(datetime.datetime.now() + datetime.timedelta(days=1))]
    elif(isthere(text, ["เมื่อวาน", "เป็น", "วัน", "อะไร"])or isthere(text, ["เมื่อวาน", "วัน", "อะไร"])):
        return ["เมื่อวานเป็น" +getweekday(datetime.datetime.now() + datetime.timedelta(days=-1))]

    
    
    # calculator
    elif(isthere(text, ["="]) or isthere(text, ["เท่ากับ"])):
        for i in range(len(text)):
            text[i] = text[i].replace(',', '')
        if((text[len(text)-1] == "เท่าไหร่") or (text[len(text)-1] == "เท่าไร")):
            try:
                return [str(sympy.sympify(calculate(text[0:len(text)-2])))]
            except:
                return ["คำถามผิด"]
        else:
            try:
                return [str(sympy.sympify(calculate(text[0:len(text)-1])))]
            except:
                return ["คำถามผิด"]
    # action       
    elif(isthere(text, ["ยก", "ปีกขวา"]) or isthere(text, ["ยก", "แขนขวา"]) or isthere(text, ["ยกมือ", "ขวา"])):
        return ["none", "none", "right_raise"]
    elif(isthere(text, ["ยก", "ปีกซ้าย"]) or isthere(text, ["ยก", "แขน", "ซ้าย"]) or isthere(text, ["ยกมือ", "ซ้าย"])):
        return ["none", "none", "left_raise"]
    elif(isthere(text, ["ยกมือ"]) or isthere(text, ["ชูมือ"])):
        return ["none", "none", "both_raise"]
        
    elif(isthere(text, ["ยกมือ", "ลง"]) or isthere(text, ["เอา", "มือ", "ลง"])):
        return ["none", "none", "default"]
        
    elif(isthere(text, ["โบกมือ", "ขวา"]) or isthere(text, ["โบก", "แขนขวา"])):
        return ["none", "none", "right_wave"]
    elif(isthere(text, ["โบกมือ", "ซ้าย"]) or isthere(text, ["โบก", "แขน", "ซ้าย"])):
        return ["none", "none", "left_wave"]
    elif(isthere(text, ["โบกมือ"]) or isthere(text, ["สะบัด", "มือ"])):
        return ["none", "none", "both_wave"]   
        
    elif(isthere(text, ["กางแขน"])):
        return ["none", "none", "extendarm"]
    elif(isthere(text, ["บิน"]) or isthere(text, ["กระพือปีก"])):
        return ["none", "none", "fly"]
    elif(isthere(text, ["ออกกำลังกาย"])):
        return ["none", "none", "exercise"]
    
    
    if(isthere(text, ["ทำไม"]) or isthere(text, ["อะไร"]) or isthere(text, ["เมื่อไร"])):
        return ["ไม่รู้อ่ะ"]
    
    
def game(text, context):

    if(len(context) > 1 and context[1] == "เกมเสียงอะไร"):
        return playgame("เกมเสียงอะไร", text, context)    
    elif(len(context) > 1 and context[1] == "เกมบวกลบเลข"):
        return playgame("เกมบวกลบเลข", text, context)     
    elif(len(context) > 1 and context[1] == "เกมอะไรต่างจากพวก"):
        return playgame("เกมอะไรต่างจากพวก", text, context)
        
    else:
        if(isthere(text, ["เกม", "เสียง", "อะไร"])):
            return ["เล่น เกมเสียงอะไร พร้อมไหม", "เกม,เกมเสียงอะไร,พร้อมไหม"]
        elif(isthere(text, ["เกม", "บวก", "ลบ", "เลข"])):
            return ["เล่น เกมบวกลบเลข พร้อมไหม", "เกม,เกมบวกลบเลข,พร้อมไหม"]
        elif(isthere(text, ["เกม", "อะไร", "ต่าง", "จาก", "พวก"])):
            return ["เล่น เกมอะไรต่างจากพวก พร้อมไหม", "เกม,เกมอะไรต่างจากพวก,พร้อมไหม"]
        elif(isthere(text, ["เล่น", "เกม"])):
            return ["เล่นเกมอะไร", "เกม"]
        elif(isthere(text, ["มี", "เกม", "อะไร"])):
            return ["มี เกมเสียงอะไร เกมบวกลบเลข เกมอะไรจากต่างพวก", "เกม"]
            
    return [" "]
    

def playgame(game, text, context):

    #start
    if(context[2] == "พร้อมไหม" or context[2] == "เล่นอีกไหม"):
    
        for i in range(len(text)):
            if(isthere(text, ["ไม่", "เล่น"])):
                return ["ไม่เล่นแล้วเหรอ"]
            elif(text[i] == "หอม" or text[i] == "พร้อม" or (i+1 < len(text) and text[i] == "เอา" and text[i-1] == "เลย") or text[i] == "เล่น"):
            
                if(game == "เกมเสียงอะไร"):
                    ques, ans = game001()
                elif(game == "เกมบวกลบเลข"):
                    ques, ans = game002()
                elif(game == "เกมอะไรต่างจากพวก"):
                    ques, ans = game003()
                else:
                    ques, ans = [" ", " "]
                return [ques, "เกม," + game + "," + ques + "," + ans]
                
        else: # quit
            return ["ไม่เล่นแล้วเหรอ"]
    # answer            
    else:
        
        for i in range(len(text)):

            if(len(context) > 2 and text[i] == context[3]):
                return ["ถูกต้อง เล่นอีกไหม", "เกม," +game+ ",เล่นอีกไหม"]
                
            elif(isthere(text, ["เปลี่ยน"])):
            
                if(game == "เกมเสียงอะไร"):
                    ques, ans = game001()
                elif(game == "เกมบวกลบเลข"):
                    ques, ans = game002()
                elif(game == "เกมอะไรต่างจากพวก"):
                    ques, ans = game003()
                else:
                    ques, ans = [" ", " "]
                    
                return [ques, "เกม," + game + "," + ques + "," + ans]
                
            elif(isthere(text, ["ฟัง", "ใหม่"]) or isthere(text, ["ขอ", "อีก"]) or isthere(text, ["เอา", "ใหม่"])):
                return [context[2], "เกม," + game + ","+ context[2] + "," + context[3]]
                
            elif(text[i] == "ยอมแพ้" or text[i] == "เฉลย"):  
                return ["คำตอบคือ "+context[3]+ " เล่นอีกไหม", "เกม," + game + ",เล่นอีกไหม"]
                
            elif(isthere(text, ["ไม่"])):
                return ["ไม่เล่นแล้วเหรอ"]
            
            else:
                return ["ผิด", "เกม," + game + "," + context[2] + "," + context[3]]
        
    return [" "]
                    
def game001():
         
    with open('json/game001.json') as data_file:    
        data = json.load(data_file)

    ran = random.randrange(0, len(data))
    return [data[ran]['sound_path'].encode('utf-8'), data[ran]['answer'].encode('utf-8')]

def game002():
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    if(random.randrange(0, 2) == 1):
        oper = "+"
    else:
        oper = "-"
        
    if(num1 > num2):
        ques = str(num1)+" "+oper+" "+str(+num2)
    else:
        ques = str(num2)+" "+oper+" "+str(num1)
    
    ans = str(sympy.sympify(ques))
    ques = ques + " เท่ากับเท่าไร"
    return [ques, ans]

def game003():

    with open('json/game003.json') as data_file:    
        data = json.load(data_file)

    rantype1 = random.randrange(0, len(data))
    rantype2 = random.randrange(0, len(data))
    while(rantype1 == rantype2):
        rantype2 = random.randrange(0, len(data))

    ranthing1 = random.randrange(0, len(data[rantype1]['name']))
    ranthing2 = random.randrange(0, len(data[rantype1]['name']))
    while(ranthing1 == ranthing2):
        ranthing2 = random.randrange(0, len(data[rantype1]['name']))
    ranthing3 = random.randrange(0, len(data[rantype2]['name']))

    x = [data[rantype1]['name'][ranthing1].encode('utf-8'), data[rantype1]['name'][ranthing2].encode('utf-8'), data[rantype2]['name'][ranthing3].encode('utf-8')]
    random.shuffle(x)
    ques = x[0] + " " + x[1] + " " + x[2]
    ans = data[rantype2]['name'][ranthing3].encode('utf-8')
    
    return [ques, ans]

if __name__ == "__main__":
    
    if(len(sys.argv) < 3):
        sys.exit()
        
    text = sys.argv[1].split()
    context = sys.argv[2].split(',')

    if(isthere(context, ["เกม"])):
        output = game(text, context)
    else:
        output = main(text, context)

    action_output = ""
    sound_output = ""

    # output sound file
    if(output[0] != "none"):
        with open('json/sound.json') as sound_file:
            sound = json.load(sound_file)

        word = output[0].split()

        for i in range(len(word)):
            for j in range(len(sound)):
                if(word[i] == sound[j]['text'].encode('utf-8')):
                    sound_output = sound_output + sound[j]['file'] + " "


    # output action order
    if(len(output) > 2):
        with open('json/action.json') as action_file:
            action = json.load(action_file)

        for i in range(len(action)):
            if(output[2] == action[i]['name']):
                action_output = action[i]['command']
    
    if not action_output:
        action_output = "none"
    if not sound_output:
        sound_output = "none"
        
    if(len(output) == 1):
        print output[0]        # text
        print "none"           # context
        print action_output    # action
        print sound_output     # sound
        
    elif(len(output) == 2):
        print output[0]
        print output[1]
        print action_output
        print sound_output
    else:
        print output[0]
        print output[1]
        print action_output
        print sound_output




