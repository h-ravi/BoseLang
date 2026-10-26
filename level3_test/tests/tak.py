import time

def tak(x, y, z):
    if y < x:
        return tak(tak(x - 1, y, z), tak(y - 1, z, x), tak(z - 1, x, y))
    return z

start = time.perf_counter()
res = tak(21, 14, 7)
end = time.perf_counter()

print("RESULT:", res)
print("TIME:", (end - start) * 1000.0)
