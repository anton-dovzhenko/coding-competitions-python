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


def sum_factors(n):
    s = 1
    rt = int(n ** 0.5)
    for i in range(2, rt + 1):
        if n % i == 0:
            s += i + (0 if i == n / i else n / i)
    return int(s)
