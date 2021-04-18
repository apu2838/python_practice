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
# import math
# import os
# import random
# import re
# import sys

if __name__ == '__main__':
    n = int(input().strip())
if n % 2 > 0:
    print("Weird")
elif n > 1 and n < 6:
    print("Not Weird")
elif n > 5 and n < 21:
    print("Weird")
elif n > 20:
    print("Not Weird")
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

#  Chapter: Loop

"""
n = 1
while n <= 1000:
	print(n)
	n = n+1
"""

"""
n = 1
temp = 0
while n <= 100:
	temp = temp + n
	n = n + 1
print(temp)
"""
"""
n = 100
temp = n*(n+1)
temp = temp/2
print(temp)
"""

"""
n = 1
temp = 0
while n <= 97:
        temp = temp + n
        n = n + 2
print(temp, "$$")
"""

"""
a = ['onion', 'potato', 'ginger', 'cucumber']
print(type(a))
for item in a:
	print(item)
"""

"""
a = {'name' : 'Shafayet', 'nickname' : 'Apu', 'email' : 'apu2048@gmail.com', 'phone' : '01755667788'}
print(a)
print(type(a))
for item in a:
	print(item)
"""

"""
a = 'Python'
for letter in a:
	print(letter)
"""

"""
# print(list(range(5, 21, 2)))
for number in range(1, 11):
	print(number)
"""

# Loop Control Statement

"""
for number in range(1, 11):
	if number == 5:
		break
	print(number)
"""

"""
for number in range(1, 11):
	if number == 5:
		continue
	print(number)
"""

"""
for number in range(1, 11):
	if number == 5:
		pass
	print(number)
"""

"""
print('Starting loop')
n = 1
while n <= 10:
	print(n)
	n = n + 1
else:
	print('Loop is over')
"""

"""
for n in range(0, 11):
	print(n)
	n = n + 1
else:
	print('The loop is over.')
"""

"""
print("Please, input the number: ")
number  = int(input())
count = 1
while count <= 10:
	print(number, 'x' , count, '=', number*count)
	count += 1

"""

"""
my_list = []

for i in range(1, 101):
	if i%3 == 0 and i%5 != 0:
		my_list.append(i)
print(my_list)
"""

"""
a = [13, 34, 19, 28, 46, 61, 73, 49, 1, 31, 4, 7, 91, 58, 52, 82, 70, 43, 88, 55, 97, 16, 22, 25, 79, 85, 40, 64, 94, 67, 37]
my_list = []

for i in a:
	if i < 50:
		my_list.append(i)

print(my_list)
"""

"""
a = [40, 45, 33, 34, 8, 38, 28, 22, 1, 7, 49, 41, 14, 5, 22, 39, 15, 19, 36, 37, 43, 2, 5, 42, 46, 48, 49, 12, 48, 37, 8, 20, 30, 20, 4, 37, 27, 29, 7, 44, 15, 32, 35, 10, 28, 18, 2, 15, 36, 38]
my_list = []

for i in a:
	if i not in my_list:
		my_list.append(i)

print(my_list)
"""

"""
print('Please, input the number:')
number = int(input())
temp = number

while number > 0:
	count = temp
	while count > 0:
		print('*', end='')
		count -= 1
	print()
	number -= 1
"""
"""
print('Please input your word')
word = input()
word = word.casefold()
reversed_word = word[::-1]  # word[::-1] is used to reverse a word!

if word == reversed_word:
	print('Great! it is a pallindrome.')
else:
	print('LOL! It is not a pallindrome.')
"""

my_list = [1, 3, 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100]
print('Input the number:')
number = int(input())

first = 0
last = len(my_list)-1
found = False
cycle = 0

while first <= last and not found:
	midpoint = (first + last)//2
	if my_list[midpoint] == number:
		found = True
	else:
		if number < my_list[midpoint]:
			last = midpoint -1
		else:
			first = midpoint+1
	cycle += 1

print('Found after', cycle, 'cycle.')
