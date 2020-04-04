def get_prime_factors(n):
    factors = []
    f = 2
    while n > 1:
        if n % f == 0:
            factors.append(f)
            n /= f
        else:
            f += 1
    return factors
