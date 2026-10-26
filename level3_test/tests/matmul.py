import time

n = 60

a = []
b = []
c = []

for i in range(1, n + 1):
    row_a = []
    row_b = []
    row_c = []
    for j in range(1, n + 1):
        row_a.append(((i * 17 + j * 31) % 100) + 1)
        row_b.append(((i * 23 + j * 13) % 100) + 1)
        row_c.append(0)
    a.append(row_a)
    b.append(row_b)
    c.append(row_c)

start = time.perf_counter()

for i in range(n):
    row_a = a[i]
    row_c = c[i]
    for j in range(n):
        s = 0
        for k in range(n):
            s += row_a[k] * b[k][j]
        row_c[j] = s

end = time.perf_counter()

total = 0
for i in range(n):
    for j in range(n):
        total = (total + c[i][j]) % 1000000007

print("RESULT:", total)
print("TIME:", (end - start) * 1000.0)
