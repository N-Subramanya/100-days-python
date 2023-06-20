# Python code to add the digits of the number entered by the user


# a = 10
# b = 20
# c = 30


# Method-3: Using General Approach: 

# Get the number
# Declare a variable to store the sum and set it to 0
# Repeat the next two steps till the number is not 0
# Get the rightmost digit of the number with help of remainder ‘%’ operator by dividing it with 10 and add it to sum.
# Divide the number by 10 with help of ‘//’ operator
# Print or return the sum

# Function to get the sum of digits 
# def getSum(n):
    
#     sum = 0
#     while (n != 0):
       
#         sum = sum + (n % 10)
#         n = n//10
       
#     return sum
   
# n = 569
# print(getSum(n))

#==========================
# Using String Character Extraction
# We will extract each character in the string input and convert it to an individual character’s integer equivalent.
# TypeError: 'int' object is not iterable

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)
    
print(f"sum is : {sum}" )