import time


def count_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            i = p * p
            while i <= n:
                is_prime[i] = False
                i += p
        p += 1

    count = 0
    for i in range(2, n + 1):
        if is_prime[i]:
            count += 1
    return count


start = time.perf_counter()

res = count_primes(50000)

end = time.perf_counter()

print("RESULT:", res)
print("TIME:", (end - start) * 1000.0)
