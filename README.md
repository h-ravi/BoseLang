<p align="center">
  <img src="logo.png" alt="BoseLang Logo" width="340" />
</p>

<h1 align="center">🇮🇳 BoseLang</h1>

<p align="center">
  <strong>A fast, fearless, and human-friendly programming language written in pure Rust.</strong><br>
  <em>Dedicated to the enduring spirit of Netaji Subhash Chandra Bose.</em>
</p>

<p align="center">
  <a href="#-key-features">Key Features</a> •
  <a href="#-performance-vs-python-314">Benchmarks</a> •
  <a href="#-quick-taste-of-boselang">Quickstart</a> •
  <a href="docs/README.md">Complete Docs</a> •
  <a href="docs/10_methods.md">Methods Guide</a> •
  <a href="docs/11_file_handling.md">Universal File I/O</a> •
  <a href="docs/12_system_and_net.md">System & Net Guide</a> •
  <a href="LEVEL_TRACKER.md">Level Roadmap</a>
</p>

---

## 🌟 Key Features

1. **Natural 1-Based Indexing:** In human life, counting starts at `1`. The 1st item is at `list[1]`, not `list[0]`. Index `0` is strictly rejected with a clear, helpful error message.
2. **Supercharged Methods & Built-ins:**
   - **Search:** `.find()` strictly returns `bool`; `.pos()` returns 1-based `Range` (`start..end`) or `int` for direct slicing `text[text.pos("sub")]`!
   - **Case & Trimming:** `.upper()`, `.lower()`, `.title()`, `.trim()`, `.ltrim()`, `.rtrim()`.
   - **Splitting & Joining:** `.split()`, `.join()` (bidirectional: `list.join("-")` and `"-".join(list)`).
   - **List Manipulations:** `.sort()`, `.reverse()`, `.pop()`, `.count()`, `.add()`, `.remove()`, `.clear()`.
3. **Universal File Engine & Memory-Safe Streaming (Level 5):**
   - **Three Clean Modes:** `read(path, limit?)` for text/slices, `read_list(path, limit?)` for lists/ranges with zero-alloc fast forward, and `read_stream(path, limit?)` for lazy streaming with constant ~8 KB RAM.
   - **Open-Ended Ranges:** `read_stream("data.csv", 2..)` streams from line 2 to EOF (skips headers effortlessly).
   - **Re-entrant Streams:** Re-run loops on the same stream variable with automatic rewind.
   - **Smart Write & Append:** `write(path, data)` & `append(path, data)` natively support both strings and lists (auto `\n`).
   - **Universal Namespace:** Direct `read()` or namespaced `file.read()`.
   - **Zero File Leaks:** Auto-closing RAII file handling with OS Protection Shield.
4. **Native System & Net Engines (Level 5):**
   - **System Engine (`system`):** `system.run(cmd)` / `run(cmd)`, `system.args()`, `system.env(key)`, `system.sleep(secs)`.
   - **Aliasing:** `fix cmd = system` gives `cmd` all system superpowers under an immutable shield.
   - **Net Engine (`net`):** Native HTTP `get(url)` and `post(url, body, headers)` for zero-setup AI & REST API communication.
5. **Native JSON Engine (`json`):**
   - **Unified Interface:** `json.read(path)` and `json.write(path, data)`.
   - **Smart Pretty-Printing:** 4-space formatted JSON writing for native Maps and Lists with auto directory creation.
   - **Smart AI Output Formatting:** Automatically parses, validates, and pretty-prints raw compact JSON strings from AI models or REST endpoints.
   - **Actionable Diagnostics:** Exact line and column syntax errors with helpful hints.
6. **Human-Centric Keywords:**
   - Conditionals: `when`, `again`, `otherwise` (no cryptic `elif`).
   - Unified Loop: `loop` handles while loops, ranges, and collections.
   - Loop Control: `stop` (break) and `skip` (continue).
   - Functions: `block name(params)` with explicit `give` returns.
   - Entry Point: `block auto main()` runs automatically on startup.
   - Immutability: `fix` locks variables or collections from mutation.
   - Type Safety & Conversion: Type locking (`int x = 10`) and dynamic/locked casting with `change x to <type>`.
7. **Smart Fail-Fast Error Diagnostics:** Actionable English error messages with helpful `Hint:` suggestions (no silent `Null` bugs, no cryptic panics).
8. **School Maths Syntax:** Write natural inequalities like `18 <= age <= 60` and `0 <= marks <= 100`.
9. **Instant Swapping & Rotation:** `a, b = b, a` and `x, y, z = y, z, x` without temporary variables.
10. **Zero-Setup Standalone Binary:** Compiles down to a single compact executable (`bose.exe`) with zero external runtime dependencies.
11. **Blazing Fast 100% Pure Bytecode VM:** Significantly faster than Python 3.14 across all compute, algorithm, and recursion benchmarks!

---

## ⚡ Performance vs Python 3.14

### Level 3 Advanced Benchmarks (`level3_test/runner.py`)
| Benchmark | Description | BoseLang Time | Python Time | Whole Process Speedup | In-Engine Speedup | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **`bst`** | Binary Search Tree Operations | ~10.6 ms | ~29.1 ms | **⚡ 2.74x faster** | **⚡ 1.25x faster** | ✓ PASS |
| **`frequency`** | Word & Character Frequencies | ~24.9 ms | ~57.3 ms | **⚡ 2.30x faster** | **⚡ 1.59x faster** | ✓ PASS |
| **`matmul`** | Matrix Multiplication | ~26.2 ms | ~52.8 ms | **⚡ 2.01x faster** | **⚡ 1.62x faster** | ✓ PASS |
| **`hanoi`** | Tower of Hanoi Recursion | ~23.2 ms | ~43.6 ms | **⚡ 1.88x faster** | **⚡ 1.18x faster** | ✓ PASS |
| **`tak`** | Deep Takeuchi Function | ~19.3 ms | ~36.4 ms | **⚡ 1.88x faster** | **⚡ 1.18x faster** | ✓ PASS |
| **`nqueens`** | N-Queens Backtracking | ~81.7 ms | ~143.1 ms | **⚡ 1.75x faster** | **⚡ 1.65x faster** | ✓ PASS |

### Level 2 Hard Compute Benchmarks (`hard_test/runner.py`)
| Benchmark | BoseLang Time | Python Time | Whole Process Speedup | In-Engine Speedup | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`collatz`** | ~87 ms | ~320 ms | **⚡ 3.64x faster** | **⚡ 3.76x faster** | ✓ PASS |
| **`primes`** | ~10 ms | ~27 ms | **⚡ 2.58x faster** | **⚡ 2.15x faster** | ✓ PASS |
| **`quicksort`** | ~10 ms | ~25 ms | **⚡ 2.57x faster** | **⚡ 1.60x faster** | ✓ PASS |
| **`mandelbrot`**| ~116 ms| ~312 ms | **⚡ 2.46x faster** | **⚡ 2.49x faster** | ✓ PASS |
| **`graph`** | ~13 ms | ~27 ms | **⚡ 1.92x faster** | **⚡ 1.53x faster** | ✓ PASS |

---

## 🚀 Quick Taste of BoseLang

```bose
/* Welcome to BoseLang! */

block auto main() {
    /* 1. Variables and String Interpolation */
    name = "Subhash"
    score = 95
    out("Namaste, {name}! Your score is {score}/100.")

    /* 2. Natural Conditionals */
    when 90 <= score <= 100 {
        out("Grade: Outstanding! 🏆")
    } again score >= 75 {
        out("Grade: Very Good! 🌟")
    } otherwise {
        out("Keep learning!")
    }

    /* 3. 1-Based Lists */
    fruits = ["Apple", "Mango", "Banana"]
    out("First fruit (index 1):", fruits[1])

    /* 4. Natural Loops with 'from' */
    loop fruit from fruits {
        out("  Enjoying:", fruit)
    }
}
```

---

## 🏃 Getting Started

### Run a Script
```powershell
.\bose.exe path\to\script.bose
```

### Run All Functional Tests
```powershell
1..6 | ForEach-Object { $name = "tests/0$($_)_*.bose"; $f = Get-ChildItem $name; .\bose.exe $f.FullName }
```

### Run Benchmarks Against Python
```powershell
python -X utf8 hard_test/runner.py
```

---

## 📚 Complete Documentation

Learn BoseLang step-by-step with zero prior experience needed:

- **[Chapter 01: Getting Started](./docs/01_getting_started.md)** — Installing `bose.exe`, writing comments, output with `out()`.
- **[Chapter 02: Variables & Types](./docs/02_variables_and_types.md)** — Types (`int`, `point`, `text`, `bool`, `Null`), and `fix`.
- **[Chapter 03: Operators & Math](./docs/03_operators_and_math.md)** — Math operators, compound assignment (`+=`), and swaps.
- **[Chapter 04: Conditionals & Decisions](./docs/04_conditionals_and_decisions.md)** — `when`, `again`, `otherwise`, and chained comparisons.
- **[Chapter 05: Loops & Ranges](./docs/05_loops_and_ranges.md)** — Condition loops, ranges (`1..10`, `5..1`, `1..10..2`), `stop`, and `skip`.
- **[Chapter 06: Blocks & Functions](./docs/06_blocks_and_functions.md)** — `block`, `give`, multiple returns, default params, and `block auto`.
- **[Chapter 07: Lists & Maps (Collections)](./docs/07_collections_lists_and_maps.md)** — Lists, Maps, 1-based indexing, slicing, and methods.
- **[Chapter 08: Built-in Tools & Error Guide](./docs/08_builtins_and_errors.md)** — Built-in functions (`len`, `type`, `clock`), errors, and fixes.
- **[Chapter 09: Shorthands & Expressive Syntax](./docs/09_shorthands_and_expressive_syntax.md)** — Concise syntax patterns and complete reference table.
- **[Chapter 10: Methods & String Superpowers](./docs/10_methods.md)** — Canonical `.find()`, `.pos()`, case/trimming, splitting, and list methods.
- **[Chapter 11: Native File I/O Engine](./docs/11_file_handling.md)** — `read`, `write`, `append`, `create`, `exist`, `delete`, and OS Protection Shield.
- **[Chapter 12: System & Net Engines](./docs/12_system_and_net.md)** — `system` (`fix cmd = system`), `run`, `args`, `env`, `sleep`, and `net` (`get`, `post`).
- **[Chapter 13: Native JSON Engine](./docs/13_json_handling.md)** — Zero-overhead JSON parsing, stringifying, query filtering, and file manipulation.
- **[Chapter 14: Level 6 Math Module & Capability Security](./docs/14_math_module.md)** — 40+ math functions across 6 categories, Bose specials, capability grants (`math(basic)`), and power transfer.
- **[Chapter 15: Level 7 Time Module & Calendar Engine](./docs/15_time_module.md)** — Human-friendly `DateTime`, 24h/12h formatting, stopwatch (`stop_timer()`), Indian Financial Year, Hindi names, and capability security.
- **[Chapter 16: Level 9 Web Server Engine](./docs/16_web_module.md)** — Pure safe Rust HTTP web server (`web.serve`), static website hosting (`req.static`), REST JSON APIs (`req.json`), CORS, and Directory Traversal Shield.
- **[Live Project: AI Chat Application](./ai_chat_project/README.md)** — Calling Groq Qwen 3.8 27B AI with native BoseLang `post()` and `.env` parsing.
- **[Live Project: imgAud_vid (Cinematic Video Generator)](./imgAud_vid/README.md)** — Converts Image + Audio into High-End Cinematic Ken Burns Video with NVIDIA NVENC GPU Acceleration.
