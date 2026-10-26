import time


def escape(cx, cy, max_iter):

    x = 0.0
    y = 0.0

    for i in range(max_iter):

        x2 = x * x
        y2 = y * y

        if x2 + y2 > 4.0:
            return i

        y = 2.0 * x * y + cy
        x = x2 - y2 + cx

    return max_iter


start = time.perf_counter()

total = 0


for py in range(1, 301):

    cy = -1.0 + (py / 300.0) * 2.0

    for px in range(1, 301):

        cx = -2.0 + (px / 300.0) * 3.0

        total += escape(cx, cy, 100)


end = time.perf_counter()


print("RESULT:", total)
print("TIME:", (end - start) * 1000.0)
