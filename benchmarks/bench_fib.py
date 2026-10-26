import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

start = time.perf_counter()
res = fib(24)
end = time.perf_counter()

elapsed_ms = (end - start) * 1000.0
print(f"[Python] fib(24): {res} | Time: {elapsed_ms:.2f} ms")
