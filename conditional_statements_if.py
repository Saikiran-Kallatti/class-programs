'''a = 10
b = 8

if a+b < 15:
    print("greater than 15")
    print("if stmt")

print("normal pgm execution")
print("main pgm")'''

'''a = 10
b = 8
if a+b < 15:
   print("greater than 15")
   print("if stmt")
else:
    print("less than 15")
    print("else stmt")
print("main pgm")
print("normal execution")'''

'''a = 10
b = 8
if a+b < 15:
   print("greater than 15")
   print("if stmt")
else:
    print("less than 15")
    print("else stmt")
print("main pgm")
print("normal execution")'''

'''
#pgm to che k whether the num is pos or neg
s = int(input("enter : "))

if s > 0:
    print("positive")
elif s == 0:
    print("number is zero")
else:
    print("number is negative")
'''

'''#pgm to check odd or even
s = int(input("enter : "))

if s%2 == 0:
    print("even")
else:
    print ("odd")'''


'''#check whether first and last chars are same in the string
s = input()

if s[0] == s[-1]:
    print("same chars")
else:
    print("not same")
'''

'''#check whether middle chars of 2 string are same or # NOTE:

one = input()
second = input()

lenone = len(one)//2
lensecond = len(second)//2

print(lenone)
if one[lenone] == second[lensecond]:
    print("same")
else:
    print("not same")
'''

#grade students
marks = int(input())

if marks < 0 or marks > 100:
    print("invalid marks")
elif marks >= 90 or marks <= 100:
    print("A+")
elif marks >=80 or marks <= 89:
    print("A")
elif marks >=70 or marks <= 79:
    print("B+")
elif marks >=60 or marks <= 69:
    print("B")
elif marks >=50 or marks <= 59:
    print("C")
else:
    print("fail")
