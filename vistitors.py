n = 163
def is_prime(n):
    smaller_primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            smaller_primes.append(num)
    return smaller_primes
print(is_prime(n))