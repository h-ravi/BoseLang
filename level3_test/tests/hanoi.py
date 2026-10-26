import time

def hanoi(n, src, dst, aux, step):
    if n == 1:
        next_step = step + 1
        next_sum = (next_step * (src + dst)) % 1000000007
        return next_step, next_sum
    s1, c1 = hanoi(n - 1, src, aux, dst, step)
    mid_step = s1 + 1
    mid_sum = (c1 + mid_step * (src + dst)) % 1000000007
    s2, c2 = hanoi(n - 1, aux, dst, src, mid_step)
    return s2, (mid_sum + c2) % 1000000007

start = time.perf_counter()
steps, checksum = hanoi(17, 1, 3, 2, 0)
end = time.perf_counter()

print("RESULT:", checksum)
print("TIME:", (end - start) * 1000.0)
