def has_digit_and_letter(string):
    has_digit = False
    has_letter = False

    # Iterate over each character in the string
    for char in string:
        if char.isdigit(): # string method
            has_digit = True
        elif char.isalpha():
            has_letter = True

        # If both a digit and a letter are found, return True
        if has_digit and has_letter:
            return True

    # If the loop completes without finding both a digit and a letter, return False
    return False

# Example usage
string1 = "abc123"  # Contains both a letter and a digit
string2 = "123456"  # Only contains digits
string3 = "abcdef"  # Only contains letters

print(has_digit_and_letter(string1))  # Output: True
print(has_digit_and_letter(string2))  # Output: False
print(has_digit_and_letter(string3))  # Output: False
