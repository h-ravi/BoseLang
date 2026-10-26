import time

seed = 12345
n = 50000
seq = []
for _ in range(n):
    seed = (seed * 1103515245 + 12345) % 2147483648
    seq.append(seed % 4)

start = time.perf_counter()

counts = {}
for i in range(n - 3):
    code = seq[i] * 64 + seq[i + 1] * 16 + seq[i + 2] * 4 + seq[i + 3]
    k = str(code)
    if k in counts:
        counts[k] += 1
    else:
        counts[k] = 1

checksum = 0
for k, count in counts.items():
    checksum = (checksum + count * count) % 1000000007

end = time.perf_counter()

print("RESULT:", checksum)
print("TIME:", (end - start) * 1000.0)
