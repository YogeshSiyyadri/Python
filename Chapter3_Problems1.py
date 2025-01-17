#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:59:50 2022

@author: yogesh siyyadri
"""

#####################################################
##### Practice Problem 3.1, Page 57 #################
#####################################################

# Implement a program that requests the current temperature in degrees Fahrenheit
# from the user and prints the temperature in degrees Celsius using the formula
# celsius= (5/9) * (fahrenheit -  32)

fahrenheit = eval(input("Enter the temp in degrees F: "))
celsius = 5/9 * (fahrenheit - 32)
print ("The temp in degrees celsius is", celsius)

#####################################################
##### Practice Problem 3.2, Page 60 #################
#####################################################

# Translate these conditional statements into Python if statements:
age= 75
# (a) If age is greater 62, print 'You can get your pension benefits'.
if age > 62 :
    print ("You can get your pension benefits" )
# (b) If name is in list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], 
# print 'One of the top 5 baseball players, ever!'. list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
name = "Ruth"
if name in ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']:
    print ("One of the top 5 baseball players, ever!")
# (c) If hits is greater than 10 and shield is 0, print 'You are dead...'.
hits = 67
shield = 0
if hits > 10 and shield == 0:
    print ("You are dead...")
# (d) If atleast one of the Boolean variables north, south, east, and west is True , print
# 'I can escape.'.

north, south, west, east = True, False, True, False
if north == True or south == False or east == True or west == False:
    print ("I can escape.")
# or   
north, south, west, east = 1,0,0,0
if north or south or east or west:
    print ("I can escape.")

#####################################################
##### Practice Problem 3.3, Page 62 #################
#####################################################

# Translate these into Python if/else statements:
# (a) If year is divisible by 4, print  Could be a leap year. ; otherwise print  Definitely not
# a leap year. 
year= eval(input( "Enter the year: "))
if (year % 4 == 0):
    print ("Could be a leap year")
else:
    print ("Definitely not a leap year")

# (b) If list ticket is equal to list lottery, print  You won! ; else print  Better luck next time... 

ticket = [1,3,4,5]
lottery= [1,3,4,5]

if ticket == lottery:
    print ("You won!")
else:
    print("Better luck next time...")

#####################################################
##### Practice Problem 3.4, Page 62 #################
#####################################################

# Implement a program that starts by asking the user to enter a login id (i.e., a string).
# The program then checks whether the id entered by the user is in the 
# list ['joe', 'sue', 'hani', 'sophie'] of valid users. 
# Depending on the outcome, an appropriate message should be printed. 
# Regardless of the outcome, your function should print 'Done.' before terminating. 
name= ['joe', 'sue', 'hani', 'sophie']
login1= "joe"
login2= "john"
if login1 in [name]:
    print ("You are in")
else:
    print ("User unknown")
print ("Done!")

#####################################################
##### Practice Problem 3.5, Page 65 #################
#####################################################

# Implement a program that requests from the user a list of words (i.e., strings) and 
# then prints on the screen, one per line, all four-letter strings in the list.
# >>>
# Enter word list: ['stop', 'desktop', 'top', 'post'] stop
# post

word= eval(input("Enter word list: "))
for value in word:
    if len(value) == 4:
        print (value)

#bonus to print vowels:

name= (input("Enter your name: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for character in name:
    if character in vowels:
        print(character)

#####################################################
##### Practice Problem 3.6, Page 66 #################
#####################################################

# Write the for loop that will print these sequences of numbers, one per line, in the interactive shell.
# (a) Integers from 0 to 9 (i.e.,0,1,2,3,4,5,6,7,8,9) 
for i in range(10):
    print(i)
# (b) Integers from 0 to 1 (i.e., 0, 1)
for i in range(2):
    print(i)

#####################################################
##### Practice Problem 3.7, Page 67 #################
#####################################################

# Write the for loop that will print the following sequences of numbers, one per line.
# (a) Integers from 3 up to and including 12
for i in range(3,13):
    print(i)
# (b) Integers from 0 up to but not including 9, but with a step of 2 instead of 
# the default of 1 (i.e., 0, 2, 4, 6, 8)
for i in range(0,9,2):
    print(i)
# (c) Integers from 0 up to but not including 24 with a step of 3
for i in range(0,24,3):
    print(i)
# (d) Integers from 3 up to but not including 12 with a step of 5
for i in range(3,12,5):
    print(i)






