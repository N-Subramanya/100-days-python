# User will input (2numbers).Write a program to swap the numbers

a = int(input("Enter your first number\n"))
b = int(input("Enter your second number\n"))

temp = a
a = b
b = temp

print(f"value of a is {a}")
print(f"value of b is {b}")
