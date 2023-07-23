In Python, you can reverse a string using different approaches. Here are a few methods:

1. Using string slicing:
```python
string = "Hello, World!"
reversed_string = string[::-1]
print(reversed_string)
```

2. Using the `reversed()` function and `str.join()`:
```python
string = "Hello, World!"
reversed_string = ''.join(reversed(string))
print(reversed_string)
```

3. Using a loop:
```python
string = "Hello, World!"
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)
```

All of the above methods will output the reversed version of the input string `"Hello, World!"` as `"!dlroW ,olleH"`.

In the first method, string slicing with the step parameter `-1` (`[::-1]`) is used to create a reversed copy of the original string.

In the second method, the `reversed()` function is applied to the string, which returns an iterator of the characters in reverse order. Then, `str.join()` is used to join the reversed characters together into a single string.

The third method involves iterating over the string characters in reverse order and building the reversed string by concatenating each character to the front of the existing reversed string.

Any of these methods can be used to achieve the reversal of a string in Python.

## STEPS 

# 1. INITIALISE AN EMPTY LIST

# The append(line) statement is adding the line variable to the lines list.

lines = [], lines is an empty list. The purpose of this line is to initialize an empty list named lines that will be used to store the strings entered by the user.

# for _ in range(3):, the underscore _ is used as a convention to indicate that the *loop variable* is not going to be used within the loop. It is a way to communicate that the loop variable is irrelevant or unimportant in the context of the loop.

In this case, the loop will iterate three times because range(3) generates the sequence [0, 1, 2]. However, we are not interested in using the loop variable, so we use _ as a placeholder. 

