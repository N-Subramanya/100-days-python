A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# You can use the generate_primes function to generate a list of prime numbers up to a specific limit:
limit = 50
prime_numbers = generate_primes(limit)
print(prime_numbers)

# In Python, the range function is an upper-bound exclusive range, which means that the ending value specified in the range is not included in the resulting sequence.

For example, when you use range(2, 10), it generates the sequence of numbers [2, 3, 4, 5, 6, 7, 8, 9], and the number 10 is not part of the sequence.

===============
The term "is_prime" is a common name given to a function that checks whether a given number is a prime number or not. It is a Boolean function that returns True if the number is prime and False otherwise.

# why square root
For example, let's say we want to check whether the number 36 is prime. The square root of 36 is 6. So, we only need to check for divisors up to 6. If a divisor is not found within this range, it means that 36 is a prime number.

Using int(number**0.5) in Python is an efficient way to calculate the square root as an integer. The expression number**0.5 calculates the square root, and int() is used to convert the result to an integer, effectively truncating any decimal part. This ensures that the loop only iterates up to the integer square root.

dividend ÷ divisor = quotient

