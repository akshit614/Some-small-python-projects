# Typing speed calculator and it also calculates time


from ast import Try
from operator import length_hint
from time import *
import random as r
from turtle import clear, speed

def error(str,entered):
    error =0 
    for i in range(len(str)):
        try:
            if str[i] != entered[i]:
                error +=1 
        except :
            error +=1 
    return round(error)


def speed_t(timestrt,timeend,useript):
    time_delay = timeend-timestrt
    time_r = round(time_delay,2)
    speed = len(useript)/time_r
    return round(speed)

while True:
    ck = input("Ready to test  : yes  or  no :-")
    if ck == "yes":
        abc=["A boy is a good guy ","who have a good heart and a great mind.","Who are u how are you what are you why are you."]

        t1=r.choice(abc)
        print("*/*/*/*/*/*/* Typing speed calculation */*/*/*/*/*/*")
        print(t1)
        print()
        time_1 = time()
        testinput = input("Enter this string for speed test: ->")   
        time_2 = time()

        print("Your speed -: ",speed_t(time_1,time_2,testinput),"w/sec")
        print("Errors in your typing - ",error(t1,testinput))


        total_err = error(t1,testinput)
        speedtype = speed_t(time_1,time_2,testinput)


        # if (total_err==0 and speed_t<=10):
        #     print("You are a tping master")
        # elif (total_err<=5 and speed_t<=15):
        #     print("You are a average typer")
        # else:
        #     print("You are a worst typer")
    elif ck=="no":
        print("Thank you")
        break

    else:
        print("Wrong input")