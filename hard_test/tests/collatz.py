import time


def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


start = time.perf_counter()

total_steps = 0
for i in range(1, 50001):
    total_steps += collatz_steps(i)

end = time.perf_counter()

print("RESULT:", total_steps)
print("TIME:", (end - start) * 1000.0)
