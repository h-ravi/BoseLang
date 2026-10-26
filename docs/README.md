# 🌟 BoseLang Official Documentation

**BoseLang** is a fast, fearless, and human-friendly programming language written in pure Rust.

*Dedicated to the enduring spirit of Netaji Subhash Chandra Bose.*

If you are a beginner, a student, or someone learning to code for the first time, this documentation is made **specially for you**. You do **not** need any prior programming experience or a teacher. Everything is explained step-by-step with real-world examples and friendly explanations.

---

## 🎯 Why BoseLang? (The Philosophy)

Most traditional programming languages were created decades ago for computer hardware, not for human brains. They force you to follow unnatural rules:
- Traditional languages make you count from **0** (e.g., `list[0]` is the first item). In real life, humans always count starting from **1**!
- Traditional languages use complicated syntax, strange symbols, and cryptic error messages or silent `Null` bugs.
- Traditional languages require heavy installations, runtimes, and dozens of confusing files.

**BoseLang changes this:**
1. **Natural Human Counting:** Lists and strings start at index **1**. The 1st item is at index 1!
2. **Clean & English-like:** Plain, sensible keywords like `when`, `again`, `otherwise`, `loop`, `block`, and `give`.
3. **No Semicolons & Clean Braces:** Clean lines of code with `{}` blocks.
4. **Smart & Fail-Fast Error Diagnostics:** Actionable English error messages with helpful `Hint:` suggestions (no silent `Null` bugs, no cryptic panics).
5. **Blazing Fast Performance:** Powered by a modern custom 100% pure Bytecode Virtual Machine written in Rust that runs arithmetic, loops, and deep recursion faster than Python!
6. **Zero Installation Nightmare:** Runs as a single, standalone executable (`bose.exe`) with zero external dependencies.

---

## 📚 Complete Table of Contents

Explore the documentation chapter by chapter:

| Chapter | Topic | What You Will Learn |
| :---: | :--- | :--- |
| **[01. Getting Started](./01_getting_started.md)** | Running BoseLang | Installing `bose.exe`, running scripts, writing comments (`/* */`), and printing output with `out()`. |
| **[02. Variables & Types](./02_variables_and_types.md)** | Storing Data | Variables, data types (`int`, `point`, `text`, `bool`, `Null`), type conversions, and locking variables with `fix`. |
| **[03. Operators & Math](./03_operators_and_math.md)** | Math & Shorthands | Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), compound assignments (`+=`), swapping (`a, b = b, a`), and rotation. |
| **[04. Conditionals](./04_conditionals_and_decisions.md)** | Making Decisions | Decision making using `when`, `again`, and `otherwise`, chained comparisons (`18 <= age <= 60`), and logic (`and`, `or`, `not`). |
| **[05. Loops & Ranges](./05_loops_and_ranges.md)** | Repetition | Repeating code with `loop`, smart ranges (`1..10`, `1..10..2`, `5..1`), and controlling loops with `stop` and `skip`. |
| **[06. Blocks & Functions](./06_blocks_and_functions.md)** | Functions & Blocks | Creating reusable `block` functions, returning values with `give`, default values, `block auto` entry points, and recursion. |
| **[07. Lists & Maps](./07_collections_lists_and_maps.md)** | Collections | Lists, Maps, the **1-based indexing rule**, negative indexing, slicing, methods (`.add`, `.remove`, `.keys`), and destructuring. |
| **[08. Built-ins & Errors](./08_builtins_and_errors.md)** | Tools & Troubleshooting | Built-in functions (`len`, `type`, `clock`, `in`), golden safety rules, understanding errors, and best practices. |
| **[09. Shorthands & Syntax](./09_shorthands_and_expressive_syntax.md)** | Expressive Power | All syntax shorthands: chained comparisons, multi-swaps, destructuring, `from` membership, one-liners, and templates. |
| **[10. Methods Guide](./10_methods.md)** | String & Collection Methods | Canonical `.find()`, `.pos()`, case/trimming, splitting, and in-place list sorting/manipulations. |
| **[11. Universal File I/O](./11_file_handling.md)** | Universal File Engine | `read(path, limit?)`, `read_list()`, `read_stream()` lazy streaming, open ranges `2..`, smart `write`/`append`. |
| **[12. System & Net Engines](./12_system_and_net.md)** | OS & Internet APIs | `system` (`fix cmd = system`), `run`, `args`, `env`, `sleep`, and `net` (`get`, `post`). |
| **[13. JSON & AI Cleaner](./13_json_handling.md)** | Native JSON & AI Engine | `json.read`, `json.write`, `json.valid`, 1-based indexing, Big Data streaming (`read_stream` + `json.read`), and AI markdown auto-cleaning. |
| **[14. Level 6 Math Module](./14_math_module.md)** | Math Engine & Capabilities | 40+ functions across 6 categories (`basic`, `power`, `theory`, `stats`, `trig`, `special`), capability-based security (`math(basic)`), and power transfer. |
| **[15. Level 7 Time Module](./15_time_module.md)** | DateTime & Calendar Engine | Human-friendly `DateTime`, 24h/12h formatting, stopwatch (`stop_timer()`), Indian Financial Year, Hindi names, and capability security. |
| **[16. Level 9 Web Module](./16_web_module.md)** | Native Web Server & APIs | Zero-dependency HTTP server, `web(port, [host], [live])`, instant live hot-reload, REST JSON APIs, static & SPA hosting (`req.spa`), cookies, and dynamic routing (`req.match`). |
| **[17. Module Packager (.bosem)](./17_module_packager.md)** | Library Packaging & Distribution | `bose new_bosem <name>` project scaffolding, `bose valid <path>`, `bose pack <folder>`, binary packaging into `.bosem`, tamper protection (CRC32), and zero-friction module distribution. |
| **[Live Project: AI Chat](../ai_chat_project/README.md)** | Real-world AI Integration | Calling Groq Qwen 3.8 27B AI with native BoseLang `post()` and `.env` parsing. |
| **[Live Project: imgAud_vid](../imgAud_vid/README.md)** | Cinematic Video Generator | Image + Audio = Cinematic Ken Burns video with NVIDIA NVENC GPU hardware acceleration. |

---

## ⚡ 60-Second Quick Taste of BoseLang

Here is what a complete BoseLang program looks like:

```bose
/* Welcome to BoseLang! */

block auto main() {
    /* 1. Variables & Math */
    name = "Subhash"
    score = 95

    /* 2. String Interpolation */
    out("Namaste, {name}! Your score is {score}/100.")

    /* 3. Human-like Conditionals (when -> again -> otherwise) */
    when 90 <= score <= 100 {
        out("Grade: Outstanding! 🏆")
    } again score >= 75 {
        out("Grade: Very Good! 🌟")
    } otherwise {
        out("Keep learning!")
    }

    /* 4. Lists & 1-Based Indexing */
    fruits = ["Apple", "Mango", "Banana"]
    out("First fruit (index 1):", fruits[1])

    /* 5. Natural Loops with 'from' */
    loop fruit from fruits {
        out("  Enjoying:", fruit)
    }
}
```

**Output:**
```text
Namaste, Subhash! Your score is 95/100.
Grade: Outstanding! 🏆
First fruit (index 1): Apple
  Enjoying: Apple
  Enjoying: Mango
  Enjoying: Banana
```

---

Ready to begin? Head over to **[Chapter 01: Getting Started](./01_getting_started.md)**!
