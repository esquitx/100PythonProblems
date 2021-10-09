#!/usr/bin/env/ python3

"""
!!!
CREDIT to zhiwehu - https://github.com/zhiwehu
!!!

As shown in the zhiwehu/Python-programming-exercises on Github.

Questions are separated in levels from 1-3, 1 being the easisest, 3 the hardest
Some are very easy, but still good practice

Format
---------
Q#. LEVEL.
QUESTION.

SOLUTION
(questionfunction)

Enjoy !
"""


# Q1. 1. 
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

def q1():
    l = []
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            l.append(i)
    
    ans1 = ','.join(l)

    return ans1


# Q2. 1.
# Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 
# Then, the output should be: 40320

def aux2(n):
    """
    Calculates the factorial of n using recursion
    """
    if n == 0:
        return 1
    else:
        return n*aux2(n-1)

def q1():
    x = int(input())
    return aux2(x)

#Q3. 1.
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). 
# and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def aux3(n):
    """
    Takes every integer from 1 to n and stores with its square in a dictionary
    """

    d = {}
    for i in range(1, n+1):
        d[i] = i**2

def q3():
    x = int(input())
    return aux3(x)

#Q4. 1.
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. S
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

def q4():
    l = input().split(', ')
    return str(l) + str(" ") + str(tuple(l))


#Q5. 1. 

# Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case. 
# Also please include simple test function to test the class methods.

class q5:
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

q5object = q5()
q5object.getString()
q5object.printString()

#Q6. 2.
# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] 
# Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. 
# EXAMPLE: Let us assume the following comma separated input sequence is given to the program: 100,150,180 
# The output of the program should be: 18,22,24

import math # Use for sqrt

def q6():
    # Define fixed variables
    c = 50
    h = 30
    l = [x for x in input().split(',')]
    ans6 = []
    for d in l:
        q = math.sqrt((2*c*float(d))/h)
        ans6.append(q)
    
    return ', '.join(q)

#Q7  2. 
#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
# EXAMPLE. Suppose the following inputs are given to the program: 3,5 
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def aux7(i, j):
    ans7 = []
    ans7.append([]*j)
    for i in range(i):
        for j in range(j):
            ans7[i][j] = i*j
    
    return ans7

def q7():
    l = [int(x) for x in input().split(',')]
    return aux7(l[0], l[1])


#Q8. 2.
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. 
# Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

def aux8(l):
    words = [word for word in l]
    return words.sort()

def q8():
    l = input.split()
    return '.'.join(aux8(l))

#Q9. 2.
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
# Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

def aux9(sentence):
    words = sentence.split(" ")
    caps = []
    for word in words:
        caps.append(word.upper())
    
    return ' '.join(caps)

def q9():
    s = input()
    return aux9(s)
    

#Q10. 2
# Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again 
# Then, the output should be: again and hello makes perfect practice world           

def aux10(sentence):
    words = sentence.split(" ").sort()
    low = []
    for word in words:
        low.append(word.lower)
    return ' '.join(low)

def q10():
    s = input()
    return aux10(s)

    
"""
TESTING

"""

q1()