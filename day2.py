# Day 2

# if Statement
age = 18

if age >= 18:
    print("You are an adult.")

# if else Statement
age = 15

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

# if elif else Statement
marks = 72

if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
else:
    print("Needs improvement")


# Task 1
num = -10

if num > 0:
 print("positive")

elif num < 0:
 print("negative")

else:
   print("zero")

#Task 2
age = int(input("enter your age"))

if age < 13:
 print("Child")

elif age >= 13 and age <= 19:
 print("Teenager")

elif age >= 20 and age <= 59:
 print("Adult")

elif age > 60: 
 print("Senior")

 # or 
 age = 17

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

#Task 3
a = 12
b = 25
c = 7

if a >= b and a >= c:
    print("A is largest:", a)
elif b >= a and b >= c:
    print("B is largest:", b)
else:
    print("C is largest:", c)


# not (reverse condition) example

is_raining = False

if not is_raining:
    print("You can go outside")
else:
    print("Stay inside")
