import math


def get_prime_factors(n):
    factors = []
    f = 2
    while n > 1:
        if n % f == 0:
            factors.append(f)
            n /= f
        elif f <= 1 + n ** 0.5:
            f += 1
        else:
            f = n
    return factors


def sum_factors(n):
    s = 1
    rt = int(n ** 0.5)
    for i in range(2, rt + 1):
        if n % i == 0:
            s += i + (0 if i == n / i else n / i)
    return int(s)


def get_primes(n: int):
    primes = []
    i = 2
    while len(primes) < n:
        is_prime = True
        root = math.ceil(i ** 0.5)
        for p in primes:
            if p > root:
                break
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1
    return primes
