## Hi!
"""
name = input('What is your name?\n')
print('Hi, %s.' %name)
"""

## Age Calculation
"""
## print("Please input your birth year")
age = int(input("Please input your birth year: \n"))
print('you are now', (2021- age), 'years!')
"""

## Multiplication
"""
## print("Please input two numbers that you like to multiply. Write values using space")
#  a, b = input("Please input two numbers that you like to multiply.\n(Write values using space. Example: 7 8) \n").split()
#  Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Multiply the numbers
multiply = float(num1) * float(num2)

# Display the sum
print('The Multiplication of {0} and {1} is {2}'.format(num1, num2, multiply))

#print(int(a)*int(b))
"""

# Python Program to calculate the square root
"""
# Input from the user
num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
"""

## String manipulation
"""
# List of lanuguages in including in the variables a, b, c, d and e
a = "Bengali"
b = "English"
c = "Arabic"
d = "Spanish"
e = "French"
print('My favorite language is: %s , %s, %s, %s, and %s' %(a, b, c, d, e))
"""

## String manipulation - case
"""
print("Please write a sentence")
message = input()
print('1. in lower:', message.lower())
print('2. in upper:', message.upper())
print('3. in capitalize:', message.capitalize())
print('4. in title:', message.title())
print('5. in swapcase:', message.swapcase())
print('6. in casefold:', message.casefold())
"""

## String manipulation - number
"""
number = 4196.87468465
print(number)
print('%.2f' % number)
print('%.4f' % number)
print('%.1f' % number)
print('%.5f' % number)
"""

## String manipulation
"""
a = input("What is your mother language? \n")
b = input("What is your 2nd language? \n")
# print('My favorite languages are:', a, 'and', b)
print('My favorite languages are: %s and %s' %(a, b))  ##String formating
"""

## Play with string
"""
a = 'bangla'
print(len(a))
print(a.count('a'))
sentence = 'How can a clan cram in a clean cream can?'
print(sentence.count('c'))
print(sentence.count('c', 5))
print(sentence.count('c', 5, 9))
print(sentence.find('c'))  #using find, finding the index and got stopped on 1st found index
print(sentence.find('c', 5))
print(sentence.find('x'))  # find returns -1 when the given value is not found
print(sentence.index('x'))  # index returns value error when the given value is not found
"""
"""
sentence = 'How can a clan cram in a clean cream can?'
#print(sentence.replace('c', 'd'))
#print(sentence.replace('?', ''))
#print(sentence.strip('?')) #Return a copy of the string with the leading and trailing characters removed.
print(sentence.split(' '))  #Actually a list.
"""

# Chapter: List
"""
# a =['onion', 'potato', 'ginger', 'cucumber']
# print(a)
# print(type(a))
# print(a[2])
# b = ['onion', 'potato', 'ginger', 'cucumber', 1, 7.1424]
# c = ['word', 'excel', 'power-point']
# d = ['chair', 'table', 'bookshelf']
# print(b)
# print(c)
# print(d)
# print(type(b))
# print(b[1:5])
# print(type(b[5]))
# b.append('tomato')  # Will add item at the end of the list
# b.insert(1,'tomato')  # To add at specific index but only one item
# b.extend(['a', 'b', 'c']) # To add multiple item in the list, put as a list
# b = b + ['x', 'y', 'z']  # Plain way to just using the addition
# a = b + c + d  # adding multiple list together
# del b[3]
# b.remove('potato')
# del b[-3]
#print (b.pop()) # will show the last item name and remove it
# print("count the total item quantity in the list:", len(b))
# print("count a specific item quantity in the list: ", b.count('potato'))
# b.reverse()
b = ['onion', 'potato', 'ginger', 'cucumber', ':', 'x', 'a']
print(b)
b.sort()
print("List updated after sorting: ", b)
"""

## Chapter: Tuple
"""
# a = ()
# a = ('onion', 'potato', 'ginger', 'cucumber')
# print(type(a))
# print(a)
b = ('onion', 'potato', 'ginger', 'cucumber', 1, 3.1416)
c = ('potato', 'a', 'b', 'potato', 'potato')
print(type(b))
print("print of variable b: ", b)
print("print of variable c: ", c)
# print("Index 0 ", b[0])
# print("Index 1 ", b[1])
# print("Index 1:5  ", b[1:5])
# print("Index :5 ", b[:5])
# print("Index 2: ", b[2:])
# print("data type of index 0 ", type(b[0]))
# print("data type of index 4 ", type(b[4]))
# print("data type of index 5 ", type(b[5]))
# b = b + ('new',)  # adding a new tuple with b and creating new tuple as tuple doesnot allow to  edit
print("count total item qty of tuple b : ", len(b))
print("count a specific item (potato) qty in tuple b : ", b.count('potato'))
print("count a specific item (potato) qty in tuple c : ", c.count('potato'))
"""

# Chapter: Set
"""
# a = {'orange', 'banana', 'pear', 'apple'}
# print("print of set a: \n", a)
# print("print of type a: \n", type(a))
# b = set('abracadabra')
# print("print of set b: \n", b)
# print("print of type b: \n", type(b))
# A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  # item will be unique in set
# A = set()
# print("print of set A: \n", A)
# print("print of type A: \n", type(A))
# A = {}
# print("print of set A: \n", A)
# print("print of type A: \n", type(A))
# A.add('pineapple')  # To add a single item in set
# A.update({'berry', 'grape'})  # To add multiple items in set
# A.remove('apple')  # To remove an item, will show error if item was not found
# A.discard('berry')  # To remove an item, will not show error if item was not found
# A.pop()  # To remove the 1st item of a set. (pop removes last item in list)
# A.clear()  # To clear set content
A = {1, 2, 3, 4, 5}
B = {6, 7, 8}
print("print of set A: \n", A)
print("print of set B: \n", B)
C = A.union(B)  # Union of to sets
print("print of set C: \n", C)
"""

#  Chapter: Dictionary
"""
a = {'name': 'MD. Maksudur Rahman Khan', 'nickname': 'Maateen', 'email': 'maateen@outlook.com', 'phone': '01711223344'}
#b = dict()
print("print of Dictionary a: \n", a)
# print("print of type a: \n", type(a))
# a['name'] = 'Shahadat Hossain'  # Update dictionary Value
# a['petname'] = 'Palash'
# a['hometown'] = 'Tangail'
# print(a['name'])
# print(a['nickname'])
# print(a['email'])
# print(a['phone'])
# print(a['petname'])
# print(a['hometown'])
# b = {'hometown' : 'Tangail', 'fav_poet' : 'Nazrul Islam'}
# a.update(b)  # Update dictionary with another dictionary items
# del a['phone']  # To delete item from dictionary
# del a['name']
# a.clear()  # To delete all items from a dictionary
# del a  # To delete the whole dictionary
# a.copy()  # .copy returns a copy of the dictionary
# a.get('name')  # will show value of the searched key, will not show any result if no defined key is found
# a.get('name' 'baari nai!')  # will show value of the searched key and will return a default value if no key was defined
# 'name' in a  # will search key and result will be True False
# 'home' in a
# a.items()  ## will return the dictionary as a list. item are set as tuple in the list and key in 0 index an value in 1 index
a.keys()  # will return all keys of the dictionary in a list
a.values()  # will return all values of the dictionary in list
print("print dictionary keys: \n", a.keys(),"\n" "print dictionary values: \n", a.values())
"""

#  Chapter: Condition Logic
# Example (if ... else)
"""
a = 5
if a < 10:
    print('a is less than 10.')
else:
    print('a is greater than 10.')
"""

#  Example (if ... elif ... else)

"""
a = int(input('Please input a number: \n'))
if a == 5:
    print("a is equal to 5")
elif a < 5:
    print("a is less than 5")
elif a  > 5 and a < 10:
    print("a is inbetween 5 and 10.")
else:
    print("a is greater than 10")
"""

# Example- nested if
"""
a = int(input('Please input a number: \n'))
if a < 10:
     if ( a % 2) == 0:
        print("less, yes")
     else:
        print("less, no")

else:
     if (a  % 3) == 0:
        print("greater, yes")
     else:
         print("greater , no")
"""

# Problem-1 (Div by 3  and 5)
"""
number = int(input('Please input a number: \n'))
if number %3 == 0 and  number %5 == 0:
	print("Yes")
else:
	print("No")
"""

# Problem-2 (Positive or Negetive)
"""
number = float(input('Please input a number: \n'))
if number > 0:
	print('Positive')
elif number < 0:
	print('Negetive')
else:
	print("Zero")
"""

#  Problem-3 (Odd or Even)
"""
number = int(input('Please input a number: \n'))
if number %2 == 0:
	print("Even")
else:
	print("Odd")

"""

# Problem-4 (Upper of Lower Case)
"""
print("Please, input a character: ")
character = input()

if character >= 'a' and character <= 'z' :  # Used the logic of ASCII values, a-z ASCII value 97-122
	print('Lower Case')
elif character >= 'A' and character <= 'Z' :  #  A-Z ASCII is 65-90
	print('Upper Case')
else:
	print('Others')
"""

# Problem-5 (Vowel Checking)

"""
print("Please, input a character: ")
character = input()

if character >= 'a' and character <= 'z' or character >= 'A' and character <= 'Z' :
	if character in 'aeiouAEIOU' :  # Checking if the inputtted character in a e i o u
		print('Vowel')
	else:
		print('Consonent')
else:
	print('Nothing')
"""

# Problem-6 (Taka Notes counting)
"""
a = int(input('Please input your lunch bill:  \n'))

b = a   # keeping the amount in valiable b

temp = a // 1000  # Counting number of 1,000 Tk. notes  and floor division was used to skip the decimal output.
print('1,000 Tk. notes:', temp)
if  temp > 0:
	a = a%1000  # calculate the balance amount after using 1000 Tk. note
	b = a  # Keeping the balance  amount t in b variable
else:
	a = b  # No 1000 Tk. note was used, keeping amount in b variable

temp = a//500  # counting number of f 500 Tk. notes
print('500 Tk. notes:', temp)
if temp > 0 :
	a = a%500  # calculate the balance amount after using 500 Tk. note
	b = a  # Keeping the balance  amount t in b variable
else:
	a = b

temp = a//100  # Counting number of 100 notes used
print("100 Tk. notes:", temp)
if temp > 0:
	a = a%100  # calculate the balance amount after using 100 Tk. note
	b = a  # Keeping the balance  amount t in b variable
else:
	a = b

temp = a//50  # Counting number of 50 notes used
print("50 Tk. notes:", temp)
if temp > 0:
	a = a%50  # calculate the balance amount after using  50 Tk. note
	b = a  #Keeping the balance  amount t in b variable
else:
	a = b

temp = a//20  # Counting number of 20 notes used
print("20 Tk. notes:", temp)
if temp > 0:
        a = a%20  # calculate the balance amount after using  20 Tk. note
        b = a  #Keeping the balance  amount t in b variable
else:
        a = b

temp = a//10  # Counting number of 10 notes used
print("10 Tk. notes:", temp)
if temp > 0:
        a = a%10  # calculate the balance amount after using  10 Tk. note
        b = a  #Keeping the balance  amount t in b variable
else:
        a = b

temp = a//5  # Counting number of 5 notes used
print("5 Tk. notes:", temp)
if temp > 0:
        a = a%5  # calculate the balance amount after using  5 Tk. note
        b = a  #Keeping the balance  amount t in b variable
else:
        a = b

temp = a//2  # Counting number of 2 notes used
print("2 Tk. notes:", temp)
if temp > 0:
        a = a%2  # calculate the balance amount after using  2 Tk. note
        b = a  #Keeping the balance  amount t in b variable
else:
        a = b

temp = a//1  # Counting number of 1 notes used
print("1 Tk. notes:", temp)
"""

#  https://www.hackerrank.com/challenges/py-if-else/problem
"""
#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
if n % 2 > 0:
    print("Weird")
elif n > 1 and n < 6:
    print("Not Weird")
elif n > 5 and n < 21:
    print("Weird")
elif n > 20:
    print("Not Weird")
else:
    print("")
"""    

#  https://www.hackerrank.com/challenges/python-division/problem
"""
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(int(a//b))
print(float(a/b))
"""