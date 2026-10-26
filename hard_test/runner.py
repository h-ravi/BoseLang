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

# Change this if required.
BOSE_EXE = Path(
    r"D:\HTML_PROJECT\BoseLang\bose.exe"
)

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

    elapsed_ms = (
        end - start
    ) / 1_000_000

    return {
        "returncode": process.returncode,
        "time": elapsed_ms,
        "output": process.stdout
    }


# ============================================================
# OUTPUT PARSING
# ============================================================

def parse_output(output):

    result_match = re.search(
        r"RESULT:\s*(.+)",
        output
    )

    time_match = re.search(
        r"TIME:\s*([0-9.eE+-]+)",
        output
    )

    result = None

    if result_match:
        result = result_match.group(1).strip()

    engine_time = None

    if time_match:
        engine_time = float(
            time_match.group(1)
        )

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
        "stdev": (
            statistics.stdev(values)
            if len(values) > 1
            else 0
        )
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
    print(
        color(
            BOLD,
            f"  {name}"
        )
    )
    print("=" * 72)


    bose_command = [
        str(BOSE_EXE),
        str(bose_file)
    ]

    python_command = [
        sys.executable,
        str(python_file)
    ]


    # --------------------------------------------------------
    # Warmup
    # --------------------------------------------------------

    print(
        color(
            CYAN,
            "\nWarmup..."
        )
    )

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


    print(
        f"\nMeasured runs: {RUNS}"
    )


    for run in range(1, RUNS + 1):

        bose = run_process(
            bose_command
        )

        python = run_process(
            python_command
        )


        # ---------------------------------------------
        # BoseLang
        # ---------------------------------------------

        if bose["returncode"] != 0:

            bose_failed = True

            print(
                color(
                    RED,
                    f"\n❌ BoseLang failed on run {run}"
                )
            )

            print(
                bose["output"]
            )

        else:

            result, engine_time = (
                parse_output(
                    bose["output"]
                )
            )

            bose_wall.append(
                bose["time"]
            )

            if engine_time is not None:
                bose_engine.append(
                    engine_time
                )

            if result is not None:
                bose_result = result


        # ---------------------------------------------
        # Python
        # ---------------------------------------------

        if python["returncode"] != 0:

            python_failed = True

            print(
                color(
                    RED,
                    f"\n❌ Python failed on run {run}"
                )
            )

            print(
                python["output"]
            )

        else:

            result, engine_time = (
                parse_output(
                    python["output"]
                )
            )

            python_wall.append(
                python["time"]
            )

            if engine_time is not None:
                python_engine.append(
                    engine_time
                )

            if result is not None:
                python_result = result


        # ---------------------------------------------
        # Run display
        # ---------------------------------------------

        print(
            f"Run {run:2d} | "
            f"BoseLang: "
            f"{bose['time']:9.3f} ms | "
            f"Python: "
            f"{python['time']:9.3f} ms"
        )


    # ========================================================
    # CORRECTNESS
    # ========================================================

    print()
    print(
        color(
            BOLD,
            "CORRECTNESS"
        )
    )


    if bose_failed:

        print(
            color(
                RED,
                "  ❌ BoseLang FAILED"
            )
        )

        print(
            "     Benchmark is INVALID."
        )

        print(
            "     Speed comparison skipped."
        )

        return {
            "status": "invalid",
            "speed": None
        }


    if python_failed:

        print(
            color(
                RED,
                "  ❌ Python FAILED"
            )
        )

        print(
            "     Benchmark is INVALID."
        )

        return {
            "status": "invalid",
            "speed": None
        }


    if (
        bose_result is not None
        and python_result is not None
        and bose_result == python_result
    ):

        print(
            color(
                GREEN,
                "  ✓ PASS"
            )
        )

        print(
            f"  Result: {bose_result}"
        )

    else:

        print(
            color(
                RED,
                "  ❌ FAIL"
            )
        )

        print(
            f"  BoseLang: {bose_result}"
        )

        print(
            f"  Python:   {python_result}"
        )

        print(
            "\n  Speed comparison skipped."
        )

        return {
            "status": "incorrect",
            "speed": None
        }


    # ========================================================
    # PROCESS TIMING
    # ========================================================

    print()
    print(
        color(
            BOLD,
            "WHOLE PROCESS TIME"
        )
    )


    print_stats(
        "BoseLang",
        bose_wall
    )

    print_stats(
        "Python",
        python_wall
    )


    bose_median = statistics.median(
        bose_wall
    )

    python_median = statistics.median(
        python_wall
    )


    ratio = (
        python_median
        / bose_median
    )


    if ratio > 1:

        print()
        print(
            color(
                GREEN,
                f"  ⚡ BoseLang: "
                f"{ratio:.2f}x faster"
            )
        )

    else:

        print()
        print(
            color(
                YELLOW,
                f"  ⚡ Python: "
                f"{1 / ratio:.2f}x faster"
            )
        )


    # ========================================================
    # ENGINE TIMING
    # ========================================================

    if bose_engine and python_engine:

        print()
        print(
            color(
                BOLD,
                "IN-ENGINE TIME"
            )
        )

        print_stats(
            "BoseLang",
            bose_engine
        )

        print_stats(
            "Python",
            python_engine
        )


        bose_engine_median = (
            statistics.median(
                bose_engine
            )
        )

        python_engine_median = (
            statistics.median(
                python_engine
            )
        )


        engine_ratio = (
            python_engine_median
            / bose_engine_median
        )


        if engine_ratio > 1:

            print(
                color(
                    GREEN,
                    f"\n  ⚡ BoseLang engine: "
                    f"{engine_ratio:.2f}x faster"
                )
            )

        else:

            print(
                color(
                    YELLOW,
                    f"\n  ⚡ Python engine: "
                    f"{1 / engine_ratio:.2f}x faster"
                )
            )


    return {
        "status": "passed",
        "speed": ratio
    }


# ============================================================
# DISCOVER TESTS
# ============================================================

def discover_tests():

    tests = []

    for bose_file in sorted(
        TESTS.glob("*.bose")
    ):

        python_file = (
            bose_file.with_suffix(".py")
        )

        if not python_file.exists():

            print(
                color(
                    YELLOW,
                    f"⚠ Missing Python pair: "
                    f"{python_file.name}"
                )
            )

            continue


        tests.append(
            (
                bose_file.stem,
                bose_file,
                python_file
            )
        )


    return tests


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print(
        color(
            BOLD,
            "╔══════════════════════════════════════════════════════════════╗"
        )
    )

    print(
        color(
            BOLD,
            "║              BOSELANG BENCHMARK RUNNER                    ║"
        )
    )

    print(
        color(
            BOLD,
            "╚══════════════════════════════════════════════════════════════╝"
        )
    )


    print()
    print(
        f"BoseLang: {BOSE_EXE}"
    )

    print(
        f"Tests:    {TESTS}"
    )

    print(
        f"Warmups:  {WARMUPS}"
    )

    print(
        f"Runs:     {RUNS}"
    )


    # --------------------------------------------------------
    # Check executable
    # --------------------------------------------------------

    if not BOSE_EXE.exists():

        print()
        print(
            color(
                RED,
                "❌ BoseLang executable not found:"
            )
        )

        print(
            BOSE_EXE
        )

        return


    # --------------------------------------------------------
    # Discover
    # --------------------------------------------------------

    tests = discover_tests()


    if not tests:

        print()
        print(
            color(
                RED,
                "❌ No benchmark tests found."
            )
        )

        return


    print()
    print(
        f"Found {len(tests)} benchmark(s)."
    )


    results = []


    # --------------------------------------------------------
    # Run
    # --------------------------------------------------------

    for name, bose_file, python_file in tests:

        result = run_test(
            name,
            bose_file,
            python_file
        )

        results.append(
            (
                name,
                result
            )
        )


    # ========================================================
    # FINAL REPORT
    # ========================================================

    print()
    print("=" * 72)
    print(
        color(
            BOLD,
            "FINAL REPORT"
        )
    )
    print("=" * 72)


    passed = 0
    invalid = 0
    incorrect = 0


    for name, result in results:

        status = result["status"]


        if status == "passed":

            passed += 1

            speed = result["speed"]

            if speed > 1:

                text = (
                    f"✓ PASS   "
                    f"{name:<25} "
                    f"BoseLang {speed:.2f}x"
                )

            else:

                text = (
                    f"✓ PASS   "
                    f"{name:<25} "
                    f"Python {1 / speed:.2f}x"
                )

            print(
                color(
                    GREEN,
                    text
                )
            )


        elif status == "invalid":

            invalid += 1

            print(
                color(
                    RED,
                    f"⚠ INVALID {name:<25} "
                    f"speed skipped"
                )
            )


        else:

            incorrect += 1

            print(
                color(
                    RED,
                    f"❌ FAIL   {name:<25} "
                    f"speed skipped"
                )
            )


    print()
    print(
        f"Passed   : {passed}"
    )

    print(
        f"Failed   : {incorrect}"
    )

    print(
        f"Invalid  : {invalid}"
    )


    print()


if __name__ == "__main__":
    main()
