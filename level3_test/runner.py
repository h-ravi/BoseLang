import subprocess
import statistics
import sys
import time
import re
from pathlib import Path


# ============================================================
# CONFIG
# ============================================================

ROOT = Path(__file__).resolve().parent
TESTS = ROOT / "tests"

BOSE_EXE = Path(r"D:\HTML_PROJECT\BoseLang\bose.exe")

WARMUPS = 2
RUNS = 5


# ============================================================
# COLORS
# ============================================================

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"


def color(code, text):
    if sys.stdout.isatty():
        return code + text + RESET
    return text


# ============================================================
# PROCESS EXECUTION
# ============================================================

def run_process(command):
    start = time.perf_counter_ns()
    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    end = time.perf_counter_ns()

    elapsed_ms = (end - start) / 1_000_000

    return {
        "returncode": process.returncode,
        "time": elapsed_ms,
        "output": process.stdout
    }


# ============================================================
# OUTPUT PARSING
# ============================================================

def parse_output(output):
    result_match = re.search(r"RESULT:\s*(.+)", output)
    time_match = re.search(r"TIME:\s*([0-9.eE+-]+)", output)

    result = None
    if result_match:
        result = result_match.group(1).strip()

    engine_time = None
    if time_match:
        engine_time = float(time_match.group(1))

    return result, engine_time


# ============================================================
# STATISTICS
# ============================================================

def stats(values):
    return {
        "min": min(values),
        "median": statistics.median(values),
        "average": statistics.mean(values),
        "max": max(values),
        "stdev": statistics.stdev(values) if len(values) > 1 else 0
    }


def print_stats(name, values):
    s = stats(values)
    print(
        f"  {name:<10}"
        f" min={s['min']:9.3f} ms"
        f" median={s['median']:9.3f} ms"
        f" avg={s['average']:9.3f} ms"
        f" max={s['max']:9.3f} ms"
        f" stdev={s['stdev']:8.3f} ms"
    )


# ============================================================
# SINGLE TEST
# ============================================================

def run_test(name, bose_file, python_file):
    print()
    print("=" * 72)
    print(color(BOLD, f"  {name}"))
    print("=" * 72)

    bose_command = [str(BOSE_EXE), str(bose_file)]
    python_command = [sys.executable, str(python_file)]

    # --------------------------------------------------------
    # Warmup
    # --------------------------------------------------------
    print(color(CYAN, "\nWarmup..."))
    for _ in range(WARMUPS):
        run_process(bose_command)
        run_process(python_command)

    # --------------------------------------------------------
    # Measured runs
    # --------------------------------------------------------
    bose_wall = []
    python_wall = []
    bose_engine = []
    python_engine = []

    bose_result = None
    python_result = None
    bose_failed = False
    python_failed = False

    print(f"\nMeasured runs: {RUNS}")

    for run_index in range(1, RUNS + 1):
        bose_run = run_process(bose_command)
        python_run = run_process(python_command)

        if bose_run["returncode"] != 0:
            print(color(RED, f"\n❌ BoseLang failed on run {run_index}"))
            print(bose_run["output"])
            bose_failed = True
            break

        if python_run["returncode"] != 0:
            print(color(RED, f"\n❌ Python failed on run {run_index}"))
            print(python_run["output"])
            python_failed = True
            break

        bose_res, bose_eng = parse_output(bose_run["output"])
        python_res, python_eng = parse_output(python_run["output"])

        if bose_res is None or bose_eng is None:
            print(color(RED, f"\n❌ BoseLang invalid output on run {run_index}"))
            print(bose_run["output"])
            bose_failed = True
            break

        if python_res is None or python_eng is None:
            print(color(RED, f"\n❌ Python invalid output on run {run_index}"))
            print(python_run["output"])
            python_failed = True
            break

        bose_result = bose_res
        python_result = python_res

        bose_wall.append(bose_run["time"])
        python_wall.append(python_run["time"])
        bose_engine.append(bose_eng)
        python_engine.append(python_eng)

        print(
            f"Run {run_index:2d} | "
            f"BoseLang: {bose_run['time']:9.3f} ms | "
            f"Python: {python_run['time']:9.3f} ms"
        )

    if bose_failed or python_failed:
        return {"status": "FAILED", "name": name}

    # --------------------------------------------------------
    # Correctness check
    # --------------------------------------------------------
    print(color(BOLD, "\nCORRECTNESS"))

    if bose_result == python_result:
        print(color(GREEN, "  ✓ PASS"))
        print(f"  Result: {bose_result}")
        correct = True
    else:
        print(color(RED, "  ❌ FAIL (Result Mismatch)"))
        print(f"  BoseLang : {bose_result}")
        print(f"  Python   : {python_result}")
        correct = False

    # --------------------------------------------------------
    # Whole process stats
    # --------------------------------------------------------
    print(color(BOLD, "\nWHOLE PROCESS TIME"))
    print_stats("BoseLang", bose_wall)
    print_stats("Python", python_wall)

    bose_wall_stats = stats(bose_wall)
    python_wall_stats = stats(python_wall)

    if bose_wall_stats["median"] < python_wall_stats["median"]:
        factor = python_wall_stats["median"] / bose_wall_stats["median"]
        winner = f"⚡ BoseLang: {factor:.2f}x faster"
        color_choice = GREEN
    else:
        factor = bose_wall_stats["median"] / python_wall_stats["median"]
        winner = f"⚡ Python: {factor:.2f}x faster"
        color_choice = YELLOW

    print(color(color_choice, f"\n  {winner}"))

    # --------------------------------------------------------
    # In-engine stats
    # --------------------------------------------------------
    print(color(BOLD, "\nIN-ENGINE TIME"))
    print_stats("BoseLang", bose_engine)
    print_stats("Python", python_engine)

    bose_eng_stats = stats(bose_engine)
    python_eng_stats = stats(python_engine)

    if bose_eng_stats["median"] < python_eng_stats["median"]:
        factor = python_eng_stats["median"] / bose_eng_stats["median"]
        winner_eng = f"⚡ BoseLang engine: {factor:.2f}x faster"
        color_eng = GREEN
    else:
        factor = bose_eng_stats["median"] / python_eng_stats["median"]
        winner_eng = f"⚡ Python engine: {factor:.2f}x faster"
        color_eng = YELLOW

    print(color(color_eng, f"\n  {winner_eng}"))

    status = "PASS" if correct else "WRONG"
    return {
        "status": status,
        "name": name,
        "bose_wall": bose_wall_stats["median"],
        "python_wall": python_wall_stats["median"],
        "bose_eng": bose_eng_stats["median"],
        "python_eng": python_eng_stats["median"],
    }


# ============================================================
# MAIN DISPATCHER
# ============================================================

def main():
    print(color(CYAN, "╔══════════════════════════════════════════════════════════════╗"))
    print(color(CYAN, "║          BOSELANG LEVEL 3 BENCHMARK RUNNER                   ║"))
    print(color(CYAN, "╚══════════════════════════════════════════════════════════════╝"))
    print()
    print(f"BoseLang: {BOSE_EXE}")
    print(f"Tests:    {TESTS}")
    print(f"Warmups:  {WARMUPS}")
    print(f"Runs:     {RUNS}")

    test_dirs = sorted([f.stem for f in TESTS.glob("*.bose")])

    if not test_dirs:
        print(color(RED, "\nNo benchmarks found in tests directory."))
        sys.exit(1)

    print(f"\nFound {len(test_dirs)} Level-3 benchmark(s).")

    results = []
    for test_name in test_dirs:
        bose_file = TESTS / f"{test_name}.bose"
        python_file = TESTS / f"{test_name}.py"

        if not python_file.exists():
            print(color(RED, f"Missing Python counterpart for {test_name}"))
            continue

        res = run_test(test_name, bose_file, python_file)
        results.append(res)

    print()
    print("=" * 72)
    print(color(BOLD, "FINAL LEVEL 3 REPORT"))
    print("=" * 72)

    passed = 0
    failed = 0

    for r in results:
        status = r["status"]
        name = r["name"]
        if status == "PASS":
            passed += 1
            wall_speedup = r["python_wall"] / r["bose_wall"] if r["bose_wall"] > 0 else 0
            winner = f"BoseLang {wall_speedup:.2f}x" if wall_speedup >= 1.0 else f"Python {1/wall_speedup:.2f}x"
            print(f"{color(GREEN, '✓ PASS')}   {name:<25} {winner}")
        else:
            failed += 1
            print(f"{color(RED, '❌ FAIL')}   {name:<25}")

    print()
    print(f"Passed   : {passed}")
    print(f"Failed   : {failed}")


if __name__ == "__main__":
    main()
