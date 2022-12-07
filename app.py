#!/usr/bin/env python

import opc
import time
import sys
import random
import math

client = opc.Client('localhost:7890')


def menu():
    
    try:
        while True:
                print("\n=================================")
                print("       LED ANIMATIONS MENU    ")
                print("=================================")
                print(" [1] - Blink Blink RGB")
                print(" [2] - Simple Dot-to-Dot Animation")
                print(" [3] - Colourful Dot-to-Dot Animation")
                print(" [4] - Damage your eyes")
                print(" [5] - Disco Animation")
                print(" [6] - Mauritius Flag")
                print(" [7] - RGB Popping Animation")
                print(" [8] - Wanna play a game?")
                print(" [9] - Back and Forth Animation")
                print("[10] - Exit")
                
                choice = input("\n> ")
                print("=================================")


                if (choice == "1"):
                    rgb()
            
                elif (choice == "2"):
                    simple_dottodot()
                        
                elif (choice == "3"):
                    colourful_dottodot()

                elif (choice == "4"):
                    damage()
                        
                elif (choice == "5"):
                    disco()

                elif (choice == "6"):
                    mru_flag()

                elif (choice == "7"):
                    popping()

                elif (choice == "8"):
                    game()
                elif (choice == "9"):
                    backandforth()
                    
                elif (choice == "10"):
                    exit_animation()
                    exit()
         
                else:
                    print("\n>> [ERROR] Enter a valid number")

    except KeyboardInterrupt:
        sys.exit(menu())
        
def rgb():

    print("\nInput your RGB colour")

    r = eval(input("R: "))
    if (r < 0 or r > 255):
             print("\n>> [ERROR] Input a value between 0 and 255 inclusive")
             sys.exit(rgb())
        
    g = eval(input("G: "))
    if (g < 0 or g > 255):
             print("\n>> [ERROR] Input a value between 0 and 255 inclusive")
             sys.exit(rgb())
             
    b = eval(input("B: "))
    if (b < 0 or b > 255):
             print("\n>> [ERROR] Input a value between 0 and 255 inclusive")
             sys.exit(rgb())
    
    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)

    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")


    try:
        black = [(0, 0, 0)] * 360
        
        while True:
        
            time.sleep(0.2)
            led_colour = [(r, g, b)] * 360
            client.put_pixels(led_colour)
            time.sleep(0.2)
            client.put_pixels(black)


    except KeyboardInterrupt:

        while True:
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    rgb()

                if (choice == "2"):
                    menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")            


def simple_dottodot():

    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)
    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")



    try:
        while True:

            r = random.randint(1, 255)
            g = random.randint(1, 255)
            b = random.randint(1, 255)
        
            for x in range(0, 360):
                led_colour[x] = (r, g, b)
                time.sleep(0.01)
                client.put_pixels(led_colour)


    except KeyboardInterrupt:

        while True:
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    simple_dottodot()

                if (choice == "2"):
                    menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")



def damage():

    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")

    try:
        led_colour1 = [(0, 0, 0)] * 360
        led_colour2 = [(255, 255, 255)] * 360
    
        while True:
            time.sleep(0.01) 
            client.put_pixels(led_colour1)
            time.sleep(0.01) 
            client.put_pixels(led_colour2)

    except KeyboardInterrupt:

        while True:
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    damage()

                if (choice == "2"):
                    menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")
                

def disco():

    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")


    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)

    try:
        while True:
            
            r = random.randint(1,255)
            g = random.randint(1,255)
            b = random.randint(1,255)
            
            frame = [ (r, g, b) ] * 360
            client.put_pixels(frame)
            time.sleep(0.1)

    except KeyboardInterrupt:

        while True:
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    disco()

                if (choice == "2"):
                    menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")
                
def mru_flag():

    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")



    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)
    

    red = [(255, 0, 0)] * 360
    blue = [(0, 32, 255)] * 360
    yellow = [(255, 255, 0)] * 360
    green = [(34, 139, 34)] * 360

    try:
        while True:
            
                for x in range(0, 360):
                                    
                    client.put_pixels(red)
                    time.sleep(0.5)
                    client.put_pixels(blue)
                    time.sleep(0.5)
                    client.put_pixels(yellow)
                    time.sleep(0.5)
                    client.put_pixels(green)
                    time.sleep(0.5)


    except KeyboardInterrupt:

        while True:
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    mru_flag()

                if (choice == "2"):
                    menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")
                

def colourful_dottodot():

    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")

    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)

    try:
        while True:
           
            for x in range(0, 360): 
                r = random.randint(1,255)
                g = random.randint(1,255)
                b = random.randint(1,255)
                
                led_colour[x]=(r, g, b) 
                
                time.sleep(0.01)
                client.put_pixels(led_colour)

    except KeyboardInterrupt:

        while True:
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    colourful_dottodot()

                if (choice == "2"):
                    menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")

def popping():

    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")

    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)

    try:
        while True:

             for i in range(0, 360):

                x = random.randint(1,360)
            
             for j in range(0, 360):
                    
                r = random.randint(1,255)
                g = random.randint(1,255)
                b = random.randint(1,255)

                led_colour[x]=(r, g, b)
                
                time.sleep(0.1)
                client.put_pixels(led_colour)

    except KeyboardInterrupt:

        while True:
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    popping()

                if (choice == "2"):
                    menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")


def netherland():
    
    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)

    for x in range(0, 120):
                led_colour[x] = (255, 51, 51)
                client.put_pixels(led_colour)

    for x in range(120, 240):
                led_colour[x] = (255, 255, 255)
                client.put_pixels(led_colour)
                        
    for x in range(240, 360):
                led_colour[x] = (0, 128, 255)
                client.put_pixels(led_colour)


def russia():

    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)

    for x in range(0, 120):
                led_colour[x] = (255, 255, 255)
                client.put_pixels(led_colour)

    for x in range(120, 240):
                led_colour[x] = (51, 51, 255)
                client.put_pixels(led_colour)
                
    for x in range(240, 360):
                led_colour[x] = (255, 0, 0)
                client.put_pixels(led_colour)

def germany():


    led_colour = [(0, 0, 0)] * 360
    client.put_pixels(led_colour)

    for x in range(0, 120):
                led_colour[x] = (32, 32, 32)
                client.put_pixels(led_colour)

    for x in range(120, 240):
                led_colour[x] = (255, 0, 0)
                client.put_pixels(led_colour)
                
    for x in range(240, 360):
                led_colour[x] = (255, 255, 0)
                client.put_pixels(led_colour)

def game():

    print("\nWhich country is found in Asia?")
    print("A - Russia")
    print("B - Netherland")
    print("C - Germany")

    choice = input("\n> ")

    if (choice == "A" or choice == "a"):
        russia()
        print("\nCorrect Answer !!")
        
        while True:
            
            print("\nDo you want to run the program again or return to menu?")
            print("1 - Run the program again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    game()

            if (choice == "2"):
                menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")
        

    elif (choice == "B" or choice == "b"):
        netherland()
        print("\nWrong Answer :(")
        
        while True:
            
            print("\nDo you want to try again or return to menu?")
            print("1 - Try Again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    game()

            if (choice == "2"):
                menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")

    elif (choice == "C" or choice == "c"):
        germany()
        print("\nWrong Answer :(")
        
        while True:
            
            print("\nDo you want to try again or return to menu?")
            print("1 - Try Again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    game()

            if (choice == "2"):
                menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")

    else:

        while True:
            print("\n>> [ERROR] Choose options [A/B/C]")

            print("\nDo you want to try again or return to menu?")
            print("1 - Try Again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    game()

            if (choice == "2"):
                menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")

def menu_animation():

    grey = (32,32,32)

    yellow=(255,255,0)
    colour = (yellow)
        
    black = (0,0,0)

    time.sleep(0.2)
    led_colour=[grey]*360
        
    led_colour[1]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)
        
    led_colour[61]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[121]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[181]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[241]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[301]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[63]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[124]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[65]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[7]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[67]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[127]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[187]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[247]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[307]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    for x in range(9,16):
            led_colour[x]=yellow
            client.put_pixels(led_colour)
            time.sleep(0.2)

    for x in range(129,136):
            led_colour[x]=yellow
            client.put_pixels(led_colour)
            time.sleep(0.2)

    for x in range(309,316):
            led_colour[x]=yellow
            client.put_pixels(led_colour)
            time.sleep(0.2)


    led_colour[249]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[189]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[129]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[69]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[18]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[78]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[138]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[198]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[258]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[318]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[80]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[141]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[202]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[263]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[324]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[264]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[204]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[144]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[84]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[24]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    for x in range(326,332):
            led_colour[x]=yellow
            client.put_pixels(led_colour)
            time.sleep(0.2)

    led_colour[26]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[31]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[86]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[91]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[146]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[151]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[206]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[211]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[266]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[271]=yellow
    client.put_pixels(led_colour)
    time.sleep(0.2)
        

def exit_animation():
    
    led_colour=[(0, 0, 0)]*360
    client.put_pixels(led_colour)

    for x in range(11,17):
        led_colour[x] = (255,255,0)
        client.put_pixels(led_colour)
        time.sleep(0.2)

    led_colour[19] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[25] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    for x in range(27,34):
        led_colour[x] = (255,255,0)
        client.put_pixels(led_colour)
        time.sleep(0.2)

    for x in range(131,137):
        led_colour[x] = (255,255,0)
        client.put_pixels(led_colour)
        time.sleep(0.2)
        
    for x in range(311,317):
        led_colour[x] = (255,255,0)
        client.put_pixels(led_colour)
        time.sleep(0.2)

    for x in range(327,334):
        led_colour[x] = (255,255,0)
        client.put_pixels(led_colour)
        time.sleep(0.2)

    for x in range(147,154):
        led_colour[x] = (255,255,0)
        client.put_pixels(led_colour)
        time.sleep(0.2)

    led_colour[77] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[191] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[197] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)
    
    led_colour[257] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[251] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[71] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[80] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[84] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[142] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[202] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[262] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[322] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)  

    led_colour[87] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[207] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)

    led_colour[267] = (255,255,0)
    client.put_pixels(led_colour)
    time.sleep(0.2)


def backandforth():

    print("\n=================================")
    print(" [CTRL-C] to exit the simulation")
    print("=================================")

    led_colour=[(0, 0, 0)]*360
    client.put_pixels(led_colour)

    try:
        while True:
            r = random.randint(1,255)
            g = random.randint(1,255)
            b = random.randint(1,255)
                
            for x in range(300,360):
                led_colour[x] = (255,255,0)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in reversed(range(300,360)):
                led_colour[x] = (r,g,b)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in range(240,300):
                led_colour[x] = (255,0,0)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in reversed(range(240,300)):
                led_colour[x] = (r,g,b)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in range(180,240):
                led_colour[x] = (55,88,0)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in reversed(range(180,240)):
                led_colour[x] = (r,g,b)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in range(120,180):
                led_colour[x] = (0,0,255)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in reversed(range(120,180)):
                led_colour[x] = (r,g,b)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in range(60,120):
                led_colour[x] = (99,55,77)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in reversed(range(60,120)):
                led_colour[x] = (r,g,b)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in range(0,60):
                led_colour[x] = (87,10,25)
                client.put_pixels(led_colour)
                time.sleep(0.01)

            for x in reversed(range(0,60)):
                led_colour[x] = (r,g,b)
                client.put_pixels(led_colour)
                time.sleep(0.01)


    except KeyboardInterrupt:

        while True:
            print("\nDo you want to try again or return to menu?")
            print("1 - Try Again")
            print("2 - Return to menu")

            choice = input("\n> ")

            if (choice == "1" or choice == "2"):
                if (choice == "1"):
                    backandforth()

            if (choice == "2"):
                menu()

            else:
                print("\n>> [ERROR] Choose options [1/2]")
        

print("Please wait while program is loading..")
menu_animation()     
menu()

