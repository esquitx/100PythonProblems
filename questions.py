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

# MODULE IMPORTS

# Q6, Q21
import math # Use for sqrt

""" 
PENDING REVISION
------------------
Q11 / 

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
        self.s = input("Introduce una frase: ")
    
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
    words = set(sentence.split(" ").sort())
    low = []
    for word in list(words):
        low.append(word.lower)
    return ' '.join(low)

def q10():
    s = input()
    return aux10(s)

#Q11. 2.
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. T
# The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 
# Assume the data is input by console.

# Notes: separate numbers in the input, then compute individualy if divisible by 5 and add to list. return this list in the correct format
def aux11(nums):
    ans = []
    for n in nums:
        if int(n, 2) % 5 == 0:
            ans.append(n)

    return ', '.join()


def q11():
    numlist = [x for x in input().split(',')]

    return aux11(numlist)
    

# Q12. 2. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence on a single line

# Notes: create empty list. iterate through numbers.  check if number has even digits. appends if true. returns correctly formatted list


def aux12(n):
    check = True
    # Check all n
    while n > 0 and check:
        digit = n % 10
        if digit % 2 != 0:
            check = not check
        else:
            n = n // 10
            

def q12():
    l = []
    for i in range(1000, 3001):
        if aux12(i):
            l.append(str(i))
    
    return ', '.join(l)


# Q13. 2. 
# Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

# Notes: set counters for letters and digits. iterate string. use isalpha and isnumeric. return counters using fsring

def aux13(s):
    letters, digits = 0, 0
    for char in s:
        if char.isalpha():
            letters += 1
        elif char.isnumeric():
            digits += 1
    
    return letters, digits

def q13():
    sentence = input("Input a sentence: ")

    return f'LETTERS {aux13(sentence)[0]} DIGITS {aux13(sentence)[1]}'


# Q14. 2. 
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
# Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

# Notes. same structure as q14

def aux14(s):
    up, low = 0, 0
    for char in s:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1

    return up, low

def q14():
    sentence = input("Input a sentence: ")

    return f'UPPER CASE {aux14(sentence)[0]} LOWER CASE {aux14(sentence)[1]}'

# Q15. 2. 
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

# Notes. create sum variable. compute 10*digit and add them to the sum variable and add them to the sum variable

def aux15(n):
    sumatorio = 0
    anterior = 0
    for i in range(4):
        anterior += n*(10**i)
        sumatorio += anterior
    
    return sumatorio

def q15():
    digit = input("Input a digit (1-9)")

    return aux15(digit)

# Q17. 2. 
# Write a program that computes the net amount of a bank account based a transaction log from console input. 
# The transaction log format is shown as following: D 100 W 200

# D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 
# Then, the output should be: 500

# Notes: split the string by spaces. iterate through list 2 step. add/substract quanitity according
def q17():
    money = 0  
    opstring = input("Write your operations: ")
    operations = opstring.split(" ")

    for i in range(0, len(operations), 2):
        movement = operations[i]
        quantity = int(operations[i+1])

        if movement == "D": 
            money += quantity
        elif movement == "W":
            money -= quantity
        else: 
            pass # DO NOTHING / None

    return money
        
#Q20. 3. 
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Notes: he hecho un poco de trampas, lo intentaré mejorar
class q20:
    def __init__(self, maximo):
        self.maximo = maximo
    
    def __iter__(self):
        self.n = 7
        return self

    def __next__(self):
        if (self.n < self.maximo):
            x = self.n
            self.n += 7
            return x
        
        else:
            raise StopIteration

#Q21. 3. 
# Question A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. 
# Please write a program to compute the distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer. 
# Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 
# Then, the output of the program should be: 2

# Notes: split instructions by space. 

def q21():
    instructionstring = input("Type instructions: ")
    instructions = instructionstring.split(" ")

    # Coordinates
    xcoord = 0
    ycoord = 0

    # Interpret instructions
    for instruction in range(1, len(instructions), 2):
        movement = instructions[instruction]
        quantity = int(instructions[instruction+1])

        if movement == "UP":
            ycoord += 1
        elif movement == "DOWN":
            ycoord -= 1
        elif movement == "LEFT":
            xcoord -= 1
        elif movement == "RIGHT":
            xcoord += 1
        else: 
            pass

    return int(round(math.sqrt((xcoord**2) + (ycoord**2))))
#Q22. 3. 
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. 
# Then, the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1

# Notes. Use dictionary. USe get to return 1 if exists, +1 if it does not.
#        To sort alphanumerically, get list of frequency, then us fprint to return in correct format

def q22():
    s = input("Type your sentence: ")

    counter = {}
    for word in s.split(" "):
        counter[word] = counter.get(word, 0) + 1

    # Create list with keys
    wordlist = counter.keys()
    wordlist.sort()


    output = ""
    # Order of words don't matter, only order of frequencies
    for key in wordlist:
        output += f'{key}:{counter[key]}'

    return output

# Q23. 1. 
# Write a method which can calculate square value of number.

# Notes. MJ deserved better
def q23(n):
    return n**2

# Q25. 1. 
#  Define a class, which have a class parameter and have a same instance parameter.

class q25():
    def __init__(self):
       self.something = input("Type anything: ")

#Q28. 1. 
# Define a function that can convert a integer into a string and print it in console.

def q28(n):
    return str(n)

#
    
"""
TESTING 

"""

