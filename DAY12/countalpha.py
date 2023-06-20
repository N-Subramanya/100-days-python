# COUNT NUMBER OF TIMES ALPHABET REPEATS IN A STRING

def counts_alphabet(string, alphabet):
    count = 0

    for char in string:
        if char == alphabet:
            count += 1

    return count

s=str(input())
a=str(input())

print(counts_alphabet(s,a))