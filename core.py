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
    output = ""
    temp = date.weekday()
    if(temp == 0):
        output = output + "วันจันทร์"
    elif(temp == 1):
        output = output +"วันอังคาร"
    elif(temp == 2):
        output = output +"วันพุธ"
    elif(temp == 3):
        output = output +"วันพฤหัสบดี"
    elif(temp == 4):
        output = output +"วันศุกร์"
    elif(temp == 5):
        output = output +"วันเสาร์"
    elif(temp == 6):
        output = output +"วันอาทิตย์"
    output = output + "ที่ " + str(date.day) + " "
    temp = date.month

    if(temp == 1):
        output = output +"เดือนมกราคม "
    elif(temp == 2):
        output = output +"เดือนกุมภาพันธ์ "
    elif(temp == 3):
        output = output +"เดือนมีนาคม "
    elif(temp == 4):
        output = output +"เดือนเมษายน "
    elif(temp == 5):
        output = output +"เดือนพฤษภาคม "
    elif(temp == 6):
        output = output +"เดือนมิถุนายน "
    elif(temp == 7):
        output = output + "เดือนกรกฏาคม "
    elif(temp == 8):
        output = output +"เดือนสิงหาคม "
    elif(temp == 9):
        output = output +"เดือนกันยายน "
    elif(temp == 10):
        output = output +"เดือนตุลาคม "
    elif(temp == 11):
        output = output +"เดือนพฤศจิกายน "
    elif(temp == 12):
        output = output +"เดือนธันวาคม "

    output = output + "ปี พ.ศ." + str(date.year + 543)
    return output

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
    print question
    return sympy.sympify(question)
            

def main(text):
    


    for i in range(len(text)):
        if(i+1 < len(text) and text[i] == "วัน" and text[i+1] == "อะไร"):

            if(isthere(text, "เมื่อวาน")):
                return date(datetime.datetime.now() + datetime.timedelta(days=-1))
            elif(isthere(text, "พรุ่งนี้")):
                return date(datetime.datetime.now() + datetime.timedelta(days=1))
            else:
                return date(datetime.datetime.now())

        

    return "ไม่รู้อ่ะ"
    #date = datetime.datetime.now()
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    #print datetime.datetime.now()
    #print datetime.datetime.now().year



if __name__ == "__main__":

    if(len(sys.argv) < 2):
        sys.exit()
    text = sys.argv[1].split()
    output = main(text)
    print output
    print calculate(text)




