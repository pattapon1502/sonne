#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime
import dateparser
import sympy

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

        if(text[i] ==  "บวก"):
            question = question + "+"
        elif(text[i] == "ลบ"):
            question = question + "-" 
        elif(text[i] == "คูณ"):
            question = question + "*"
        elif(text[i] == "หาร"):
            question = question + "/"
        elif(text[i] == "ยกกำลัง"):
            question = question + "**"
        else:
            question = question + text[i]
    #print question
    return sympy.sympify(question)
            

def main(text):
    


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

    return ["ไม่รู้อ่ะ"]
    #date = datetime.datetime.now()
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    #print datetime.datetime.now()
    #print datetime.datetime.now().year
    
def game(text):

    for i in range(len(text)):
        
        if(text[i] == "เล่น" and text[i-1] == "เกม"):
            return [0, 0]



if __name__ == "__main__":

    if(len(sys.argv) < 3):
        sys.exit()
    text = sys.argv[1].split()
    context = sys.argv[2].split()
    
    if(isthere(context, "เกม")):
        output = game(text)
    else:
        output = main(text)
        
    if(len(output) == 1):
        print output[0]
        print "none"
    else:
        print output[0]
        print output[1]
    



