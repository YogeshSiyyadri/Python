#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:28:23 2022

@author: yogesh siyyadri
"""

#####################################################
##### Practice Problem 5.1, Page 130 ################
#####################################################

# Implement function myBMI() that takes as input a person’s height (in inches) and weight (in pounds) and computes the person’s Body Mass Index (BMI). The BMI formula is:
# bmi = weight ⇤ 703 height2
# Your functions should print the string 'Underweight' if bmi < 18.5, 'Normal' if 18.5 <= bmi < 25, and Overweight if bmi >= 25.
 
# >>> myBMI(190, 75)
# Normal
# >>> myBMI(140, 75)
# Underweight

def myBMI(height, weight):
    "Enter height in inches followed by weight in pounds"
    bmi= (weight * 703)/(height **2)
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print ("Normal")
    else:
        print ("Overweight")
        
#####################################################
##### Practice Problem 5.2, Page 132 ################
#####################################################

# Write a function named powers() that takes a positive integer n as input and prints, on the
# screen, all the powers of 2 from 21 to 2n. 
# >>> powers(6)
# 2 4 8 16 32 64

def powers(n):
    if n < 1:
        return ("Not a positive integer")
    else:
        for i in range(n):    #for i in range(1,n+1)
            print(2** (i+1),end = " ")
            
#####################################################
##### Practice Problem 5.3, Page 134 ################
#####################################################
            
# Write function arithmetic() that takes a list of integers as input and returns True if they form an arithmetic sequence. (A sequence of integers is an arithmetic sequence if the difference between consecutive items of the list is always the same.)
#    >>> arithmetic([3, 6, 9, 12, 15])
#    True
#    >>> arithmetic([3, 6, 9, 11, 14])
#    False
#    >>> arithmetic([3])
#    True        

def arithmetic(lst):
    if len(lst)<2:
        return True
    else:
        diff = lst[1]-lst[0]
        n=len(lst)
        for i in range(1,n-1):
            if lst[i+1]-lst[i] != diff:
                return False
        return True
    
#####################################################
##### Practice Problem 5.4, Page 136 ################
#####################################################

# Implement function factorial() that takes as input a nonnegative integer and returns its factorial. The factorial of a nonnegative integer n, denoted n!, is defined in this way:
# ⇢ 1 if n = 0 n!= n⇥(n 1)⇥(n 2)⇥...⇥2⇥1 ifn>0
# So, 0! = 1, 3! = 6, and 5! = 120.
#    >>> factorial(0)
#    1
#    >>> factorial(3)
#    6
#    >>> factorial(5)
#    120

def factorial(n):
    if n == 0:
        return 1
    else:
        num=1
        for i in range (1,n+1):
            #num= num * i  
            num *= i
        return num
        
#####################################################
##### Practice Problem 5.5, Page 136 ################
#####################################################

# An acronym is a word formed by taking the first letters of the words in a phrase and then making a word from them. For example, RAM is an acronym for random access memory. Write a function acronym() that takes a phrase (i.e., a string) as input and then returns the acronym for that phrase. Note: The acronym should be all uppercase, even if the words in the phrase are not capitalized.
# >>> acronym('Random access memory') 
# 'RAM'
#  >>> acronym('central processing unit') 
# 'CPU'

   def acronym(phrase):
       words=phrase.split()
       acr= ""
       for i in words:
           acr += i[0].upper()
       return acr
   
#####################################################
##### Practice Problem 5.6, Page 137 ################
#####################################################
        
# Write function divisors() that takes a positive integer n as input and returns the list of all positive divisors of n.
#    >>> divisors(1)
#    [1]
#    >>> divisors(6)
#    [1, 2, 3, 6]
#    >>> divisors(11)
#    [1, 11]

def divisors(n):
    div=[]
    for i in range (1,n+1):
        if n % i ==0:
            div.append(i)
    return div

#####################################################
##### Practice Problem 5.7, Page 138 ################
#####################################################

# Write a function xmult() that takes two lists of integers as input and returns a list containing all products of integers from the first list with the integers from the second list.
#    >>> xmult([2], [1, 5])
#    [2, 10]
#    >>> xmult([2, 3], [1, 5])
#    [2, 10, 3, 15]
#    >>> xmult([3, 4, 1], [2, 0])
#    [6, 0, 8, 0, 2, 0]

def xmult(list1,list2):
    lst= []
    for i in list1:
        for j in list2:
            lst.append(i*j)
    return lst
    
#####################################################
##### Practice Problem 5.8, Page 139 ################
#####################################################

# One way to sort a list of n di erent numbers in increasing order is to execute n   1 passes over the numbers in the list. Each pass compares all adjacent numbers in the list and swaps them if they are out of order. At the end of the first pass, the largest item will be the last in the list (at index n   1). Therefore, the second pass can stop before reaching the last element, as it is already in the right position; the second pass will place the second largest item in the next to last position. In general, pass i will compare pairs at indexes 0 and 1, 1 and 2, 2 and 3, . . . , and i   1 and i; at the end of the pass, the ith largest item will be at index n   i. Therefore, after pass n   1, the list will be in increasing order.
# Write a function bubbleSort() that takes a list of numbers as input and sorts the list using this approach.
#    >>> lst = [3, 1, 7, 4, 9, 2, 5]
#    >>> bubblesort(lst)
#    >>> lst
#    [1, 2, 3, 4, 5, 7, 9]

def bubblesort(lst):
    n= len(lst)
    for i in range (n-1):
        for j in range(n-(i+1)):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# i is iteration number and j is element number 

#####################################################
##### Practice Problem 5.9, Page 140 ################
#####################################################

# Write a function add2D() that takes two two-dimensional lists of same size (i.e., same num- ber of rows and columns) as input arguments and increments every entry in the first list with the value of the corresponding entry in the second list.
#    >>> t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
#    >>> s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]
#    >>> add2D(t,s)
#    >>> for row in t:
# print(row)
#    [4, 8, 4, 5]
#    [5, 2, 10, 3]
#    [8, 4, 6, 6]

def add2D(t,s):
    t_row = len(t)
    t_col = len(t[0])
    s_row = len(s)
    s_col = len(s[0])
    
    ans = []
    
    if t_row == s_row and t_col == s_col:
        for i in range(t_row):
            a_row= []
            for j in range(t_col):
                a_row.append(t[i][j] + s[i][j])
            ans.append(a_row)
        return ans
    else:
        return " Please enter 2D lists of same size"
    
#####################################################
##### Practice Problem 5.10, Page 144 ###############
#####################################################

# Write a function interest() that takes one input, a floating-point interest rate (e.g., 0.06 which corresponds to a 6% interest rate). Your function should compute and return how long (in years) it will take for an investment to double in value. Note: The number of years it takes for an investment to double does not depend on the value of the initial investment.
#    >>> interest(0.07)
#    11

def interest(rate)
    
    amount= 100
    rate= 0.06
    double= amount *2
    
    t=0
    p= amount 
    
    while p<=double:
        p= p * (1+rate)
        t+= 1
    return t
        
# or

def interest(rate)
    
    amount= 1    #does not matter what the amount is the interest is driven by rate not by the amount. So changing the amount wont change the time period, it can be $100, $1, $10000000    
    t=0
    
    while p<=2:  # its 2 since its double so 1*2 =2 
        amount= amount * (1+rate)
        t+= 1
    return t

















