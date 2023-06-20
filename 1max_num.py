# User will input (3ages).Find the oldest one

print("hello world")

# a = 3
# b = 4
# c = 5

a = int(input("Enter the first age\n"))
b = int(input("Enter the second age\n"))
c = int(input("Enter the third age\n"))

max = a

if max < b:
    max = b
if max < c:
    max = c
print(f"Maximum age is {max}")