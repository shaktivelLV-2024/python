# -*- coding: utf-8 -*-
"""shaktiAssessment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v_6vHiDYJQl3oSG_FiL-miKhuJfo4UnI
"""

#1 Area of rectangle
a=int(input("Length of the rectangle:"))
b=int(input("Breadth of the rectangle:"))
area = a*b
print("area of the rectangle:",area)

#2 BMI
a= float(input("weight in kg:"))
b= float(input("height in mts:"))
bmi = round(a/(b**2),2)
print("BMI of the person:",bmi)

#3
studentsdata ={}
n = int(input("Enter no. of students :"))
for i in range (n):
  name = input("Enter name:")
  grade = (input("Enter grade:"))
  studentsdata[name]=grade

for name,grade in studentsdata.items():
  print(f"{name}:{grade}F")

print(studentsdata)

#4
age = int(input("Enter your age : "))
if age <18:
  print("MINOR")
elif age>=18 and age<50:
  print("ADULT ")
else:
  print("SENIOR")

#5
for i in range(1,50):
  if (i%2 ==0):
    print(i)

#6

password = "1234"
entry = ""

while entry != password:
	entry = input("Please enter the password: ")

print("Correct password!")

#7
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [4, 5]
average = average(numbers)
print("The average is", average)

#8

def vowels():
  string = "Shakti"
  vowels = "aeiouAEIOU"

  count = sum(string.count(vowel) for vowel in vowels)
  print(count)

#9

import datetime as dtt

current_date = dtt.datetime.now()
print(current_date)

#10
try:
    a = int(input('Enter a'))
    b = int(input('Enter the b'))
    print(a+b)
except ValueError:
    print('Non-numeric inputsare not allowed')

#11
try:
    a = int(input('Enter an integer value'))
    print(a)
except ValueError:
    print('The value cannot be non integer')

#12
def division(a,b):
    try:
        return b/a
    except ZeroDivisionError:
        print('Division by zero not possible')

#13
f = open('shaktisfile.txt','w')
f.writelines('Hello,Python!')

#14
f = open('shaktisfile.txt','r')
f.readlines()

#15
f = open('shaktisfile.txt','a')
f.writelines('Morningggg')

f = open('shaktisfile.txt','r')
f.readlines()