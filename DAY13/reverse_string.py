# reverse string

test_string = input()
reversed_string = ''

for char in test_string:
    reversed_string = char + reversed_string

print(reversed_string)

#=============================
# if strings on multiple lines

# capture input

t=int(input())

lines = []
for _ in range(t):
    line=str(input())
    lines.append(line)

# Reverse and print the strings
for line in lines:
    reversed_line = line[::-1]
    print(reversed_line)