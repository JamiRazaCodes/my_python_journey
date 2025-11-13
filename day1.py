print("Hello, World!")

name = "Jami"
age = 21
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_student))  # <class 'bool'>

x = "2"
y = 5
print(x * y)
 
a = 8
b = 3

print(a**b)

name = input("Enter your name: ")
print("Hello", name)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Sum:", num1 - num2)
print("Sum:", num1 * num2)
print("Sum:", num1 / num2)
print("floor division:", num1 // num2)
print("Sum:", num1 ** num2)

total_minutes=int(input("Enter total minutes minutes:" ))

hours=total_minutes//60
minutes= total_minutes%60

print("hours = ", hours, "and minutes = ", minutes)