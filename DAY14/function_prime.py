# function that checks whether a given number is a prime number:
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# another function to generate a list of prime numbers up to a given limit:

def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# To check the number of prime numbers up to a given limit, you can modify the generate_primes function to count the prime numbers instead of storing them in a list. Here's how you can do it:

def count_primes_up_to(limit):
    count = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            count += 1
    return count

# calling
limit = 50
prime_numbers = generate_primes(limit)
print(prime_numbers)
