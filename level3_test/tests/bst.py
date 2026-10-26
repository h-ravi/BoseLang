import time

def new_node(val):
    return {"val": val, "left": None, "right": None}

def insert(root, val):
    if root is None:
        return new_node(val)
    if val < root["val"]:
        root["left"] = insert(root["left"], val)
    elif val > root["val"]:
        root["right"] = insert(root["right"], val)
    return root

def in_order_sum(node):
    if node is None:
        return 0
    left_sum = in_order_sum(node["left"])
    right_sum = in_order_sum(node["right"])
    return (left_sum + node["val"] + right_sum) % 1000000007

# Generate 2,000 pseudo-random numbers
seed = 42
nums = []
for _ in range(2000):
    seed = (seed * 1103515245 + 12345) % 2147483648
    nums.append((seed % 10000) + 1)

start = time.perf_counter()

root = None
for val in nums:
    root = insert(root, val)

checksum = in_order_sum(root)

end = time.perf_counter()

print("RESULT:", checksum)
print("TIME:", (end - start) * 1000.0)
