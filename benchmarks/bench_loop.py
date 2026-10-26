import time

start = time.perf_counter()

total = 0
i = 1
while i <= 500000:
    total += i
    i += 1

end = time.perf_counter()
elapsed_ms = (end - start) * 1000.0

print(f"[Python] Total: {total} | Time: {elapsed_ms:.2f} ms")
