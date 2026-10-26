import os
import subprocess
import time

def run_cmd(cmd):
    t0 = time.perf_counter()
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    t1 = time.perf_counter()
    return res.stdout.strip(), (t1 - t0) * 1000.0

print("=" * 60)
print("       BOSE LANG vs PYTHON BENCHMARK SUITE")
print("=" * 60)

# 1. Startup Time Benchmark
print("\n[1] Cold Startup Time (Empty Script / Version Check):")
py_out, py_startup = run_cmd('python -c "pass"')
bose_out, bose_startup = run_cmd('bose.exe tests/01_basics.bose')

print(f"  Python Process Startup:   {py_startup:.2f} ms")
print(f"  BoseLang Process Startup: {bose_startup:.2f} ms")

# 2. While Loop & Arithmetic (500,000 iterations)
print("\n[2] Loop & Arithmetic (500,000 iterations):")
py_loop_out, py_loop_wall = run_cmd('python benchmarks/bench_loop.py')
bose_loop_out, bose_loop_wall = run_cmd('bose.exe benchmarks/bench_loop.bose')
print(f"  {py_loop_out} (Total Process: {py_loop_wall:.2f} ms)")
print(f"  {bose_loop_out} (Total Process: {bose_loop_wall:.2f} ms)")

# 3. Recursive Fibonacci (fib(24))
print("\n[3] Recursion & Function Calls (fib(24) ~ 150,000 calls):")
py_fib_out, py_fib_wall = run_cmd('python benchmarks/bench_fib.py')
bose_fib_out, bose_fib_wall = run_cmd('bose.exe benchmarks/bench_fib.bose')
print(f"  {py_fib_out} (Total Process: {py_fib_wall:.2f} ms)")
print(f"  {bose_fib_out} (Total Process: {bose_fib_wall:.2f} ms)")

# 4. Binary & Footprint
bose_size = os.path.getsize("bose.exe") / 1024.0
print(f"\n[4] Distribution Size:")
print(f"  BoseLang Binary (bose.exe): {bose_size:.1f} KB (Single standalone .exe, zero dependencies)")
print(f"  Python Standard Install:   ~50+ MB (Requires DLLs, stdlib, runtime)")

print("\n" + "=" * 60)
