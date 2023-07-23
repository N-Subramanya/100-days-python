In Python, a function is a reusable block of code that performs a specific task or set of tasks. It allows you to encapsulate logic and functionality so that you can call it multiple times from different parts of your program without having to rewrite the same code.

A function in Python typically has the following components:

Function header: This includes the keyword def, followed by the function name, a pair of parentheses (), and optionally, any parameters that the function may accept.

Function body: This is indented below the function header and contains the actual code that defines what the function does. It can include any number of statements, calculations, or other functions.

Return statement (optional): A function can return a value using the return keyword. If a function does not have a return statement, it implicitly returns None.

def function_name(parameters):
    # Function body (code goes here)
    # ...
    # Optional: return statement
    return value
#==========================================
def add_numbers(a, b):
    result = a + b
    return result

# calling the function
sum_result = add_numbers(5, 7)
print(sum_result)  # Output: 12

================
# why return
The return keyword in Python is used to specify the value that a function should send back as a result when it is called. When a function executes a return statement, it immediately stops executing, and the value specified after the return keyword is passed back to the caller.
- passing back results
- accessing function results
- exiting early
- multiple return values(tuple)
- returning None