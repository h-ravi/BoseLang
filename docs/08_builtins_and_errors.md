# 🛠️ Chapter 08: Built-in Tools & Error Guide

In this chapter, you will find a complete reference of all built-in tools provided by BoseLang, understand common errors, and learn how to fix them effortlessly.

---

## 1. Built-in Function Reference

BoseLang comes with a standard set of built-in functions ready to use without importing anything:

### 1. `out(...)` — Display Output
Prints one or more values to the screen, separated by a single space, followed by a newline:
```bose
out("Result:", 42, true)  /* "Result: 42 true" */
```

### 2. `in(prompt)` — Read Input
Displays an optional prompt message and reads a line of text typed by the user:
```bose
name = in("What is your name? ")
out("Welcome,", name)
```

### 3. `len(collection)` — Count Items
Returns the number of elements in a list, map, string, or range:
```bose
out(len([10, 20, 30]))     /* 3 */
out(len("BoseLang"))       /* 8 */
out(len(1..5))             /* 5 */
```

### 4. `type(value)` — Inspect Type
Returns the name of the data type as a string (`"int"`, `"point"`, `"text"`, `"bool"`, `"list"`, `"map"`, `"range"`, `"Null"`):
```bose
out(type(50))              /* "int" */
out(type(3.14))            /* "point" */
out(type("Hello"))         /* "text" */
```

### 5. `int(value)` — Convert to Integer
Converts a decimal number, boolean, or numeric string into an integer:
```bose
out(int(3.85))             /* 3 (truncates decimal) */
out(int("100"))            /* 100 */
out(int(true))             /* 1 */
```

### 6. `point(value)` — Convert to Decimal
Converts an integer or numeric string into a `point` floating-point number:
```bose
out(point(25))             /* 25.0 */
out(point("3.14"))         /* 3.14 */
```

### 7. `text(value)` — Convert to Text
Converts any value into its string representation:
```bose
out(text(12345))           /* "12345" */
out(text(true))            /* "true" */
```

### 8. `bool(value)` — Convert to Boolean
Converts a value to `true` or `false`:
```bose
out(bool(1))               /* true */
out(bool(0))               /* false */
out(bool(""))              /* false (empty text is false) */
out(bool("hello"))         /* true */
out(bool(Null))            /* false */
```

### 9. `clock()` — Measure High-Precision Time
Returns the current timestamp in seconds (with microsecond precision). Ideal for benchmarking:
```bose
start = clock()

/* Some calculation */
total = 0
loop i from 1..100000 {
    total += i
}

end = clock()
elapsed_ms = (end - start) * 1000.0
out("Time taken:", elapsed_ms, "ms")
```

---

## 2. Smart Diagnostic Errors & The Fail-Fast Philosophy

BoseLang is **fail-fast and fearless**: it never hides bugs behind silent `Null` values or silent corruptions. When an error occurs, BoseLang tells you exactly what went wrong and gives you an actionable `Hint:` on how to fix it.

---

### Error 1: Index Error (Accessing Index 0)

> ❌ **Error Message:**
> ```text
> Index Error: BoseLang uses 1-based indexing; index 0 is invalid.
>   Hint: In BoseLang, counting starts at 1. Use 'list[1]' for the first item, or 'list[-1]' for the last item.
> ```

#### Why did this happen?
In human life, counting starts at `1`. BoseLang strictly follows human intuition. Index `0` does not exist for lists, maps, or strings.

#### How to fix it:
Change `items[0]` to `items[1]` for the first item, or `items[-1]` for the last item:
```bose
/* WRONG */
fruits = ["Apple", "Mango"]
out(fruits[0])  /* ❌ Index 0 is invalid */

/* CORRECT */
out(fruits[1])  /* ✅ "Apple" (first element) */
out(fruits[-1]) /* ✅ "Mango" (last element) */
```

---

### Error 2: Division by Zero

> ❌ **Error Message:**
> ```text
> Math Error: Division by zero.
>   Hint: Divisor cannot be zero in division operations.
> ```

#### Why did this happen?
Dividing by zero is mathematically undefined. BoseLang catches this before any CPU exception or NaN corruption occurs.

#### How to fix it:
Check if the divisor is non-zero before dividing:
```bose
divisor = 0

when divisor != 0 {
    out(100 / divisor)
} otherwise {
    out("Cannot divide by zero!")
}
```

---

### Error 3: Modifying a `fix` Variable

> ❌ **Error Message:**
> ```text
> Fixed Error: Cannot modify fixed variable 'max_users'.
>   Hint: Variable 'max_users' was declared with 'fix' (immutable). To allow changes, remove 'fix' from its declaration: 'max_users = ...'.
> ```

#### Why did this happen?
You declared a variable or collection with `fix`, making it strictly immutable, but later tried to reassign it or modify it with `.add()`, `.remove()`, or `+=`.

#### How to fix it:
If the variable needs to change during your program's life, remove `fix` from its declaration:
```bose
/* Mutable variable */
max_users = 100
max_users = 200  /* ✅ Works cleanly */
```

---

### Error 4: Type Lock Violation

> ❌ **Error Message:**
> ```text
> Type Error: Cannot assign 'text' value to variable 'score' which is typed as 'int'.
>   Hint: Variable 'score' was declared as 'int'. Use 'change score to text' if you wish to change its data type.
> ```

#### Why did this happen?
You declared a variable with an explicit type (e.g. `int score = 100`), which locked its type, and later tried to assign an incompatible value (like `"Passed"`).

#### How to fix it:
Either assign a matching integer value, or explicitly convert its type using `change`:
```bose
int score = 100

/* To allow changing type: */
change score to text
score = "Passed"  /* ✅ Allowed */
```

---

### Error 5: Undefined Variable (Typo Detection)

> ❌ **Error Message:**
> ```text
> Name Error: Variable 'scroe' is not defined.
>   Hint: Check your spelling or ensure the variable is defined before reading it.
> ```

#### Why did this happen?
You mistyped a variable name (like `scroe` instead of `score`) or tried to read a variable before it was defined. BoseLang will **never** silently return `Null` on typos!

#### How to fix it:
Check the spelling of your variable or ensure it is initialized before being used:
```bose
score = 100
out(score)  /* ✅ Correct spelling */
```

---

### Error 6: Scope Leakage

> ❌ **Error Message:**
> ```text
> Name Error: Variable 'temp' is not defined.
>   Hint: Check your spelling or ensure the variable is defined before reading it.
> ```

#### Why did this happen?
Variables declared inside a loop or conditional block (`{}`) are isolated to that block and destroyed when the block finishes.

#### How to fix it:
If you need to use a variable after a loop or conditional, declare it outside first:
```bose
/* Declare outside so it survives after the loop */
total = 0

loop i from 1..5 {
    total += i
}

out("Total:", total)  /* ✅ 15 */
```

---

### Error 7: Undefined Function Call

> ❌ **Error Message:**
> ```text
> Name Error: Function 'calculate()' is not defined.
>   Hint: Make sure the block is defined using 'block calculate() { ... }' before calling it.
> ```

#### Why did this happen?
You called a function name that has not been defined in your program.

#### How to fix it:
Define the block function before or after calling it:
```bose
block calculate() {
    give 42
}

out(calculate())  /* ✅ 42 */
```

---

### Error 8: Foreign Language Keyword Traps (Python, JS, C Transition)

If you are transitioning to BoseLang from Python, JavaScript, or C, BoseLang actively guides you with smart diagnostic hints when you use foreign keywords by mistake:

| Mistake in Other Languages | BoseLang Keyword | Smart Diagnostic Output |
| :--- | :--- | :--- |
| `loop a in b` | `loop a from b` | `Syntax Error: In BoseLang, collection loops use 'from', not 'in'. Hint: Change 'in' to 'from': 'loop a from ...'` |
| `if condition { ... }` | `when condition { ... }` | `Syntax Error: BoseLang uses 'when' instead of 'if'. Hint: Write 'when <condition> { ... }'` |
| `else { ... }` | `otherwise { ... }` | `Syntax Error: BoseLang uses 'otherwise' instead of 'else'. Hint: Write 'otherwise { ... }'` |
| `elif condition { ... }` | `again when condition { ... }` | `Syntax Error: BoseLang uses 'again when' instead of 'elif'. Hint: Write 'again when <condition> { ... }'` |
| `while condition { ... }` | `loop condition { ... }` | `Syntax Error: BoseLang uses 'loop <condition> { ... }' instead of 'while'. Hint: Change 'while' to 'loop'.` |
| `for item in items` | `loop item from items` | `Syntax Error: BoseLang uses 'loop item from collection { ... }' instead of 'for'. Hint: Write 'loop item from list { ... }'` |
| `def add(a, b)` | `block add(a, b)` | `Syntax Error: BoseLang defines functions using 'block', not 'def'. Hint: Write 'block name(args) { ... }'` |
| `return val` | `give val` | `Syntax Error: BoseLang uses 'give' to return values from a block, not 'return'. Hint: Write 'give value' instead of 'return value'.` |
| `break` | `stop` | `Syntax Error: BoseLang uses 'stop' to break out of a loop, not 'break'. Hint: Write 'stop' instead of 'break'.` |
| `continue` | `skip` | `Syntax Error: BoseLang uses 'skip' to skip to the next iteration, not 'continue'. Hint: Write 'skip' instead of 'continue'.` |
| `print(...)` | `out(...)` | `Name Error: Function 'print()' is not defined. Hint: In BoseLang, use 'out(...)' to print to the screen.` |
| `list.push(x)` / `.append(x)` | `list.add(x)` | `Name Error: Method '.push()' does not exist. Hint: In BoseLang, use '.add(...)' to append items to a list.` |
| `True` / `False` | `true` / `false` | `Name Error: 'True' is not defined. Hint: In BoseLang, booleans are lowercase: use 'true'.` |
| `None` / `null` | `Null` | `Name Error: 'None' is not defined. Hint: In BoseLang, null is capitalized: use 'Null'.` |

---

## 3. Best Practices for Writing Clean BoseLang

1. **Use clear names:** Name variables and blocks after what they represent (e.g. `student_name`, `calculate_total`).
2. **Comment your thoughts:** Use `/* ... */` to leave notes for yourself and others.
3. **Take advantage of string interpolation:** Write `"{user} scored {score}"` instead of messy `+` concatenation.
4. **Embrace 1-based indexing:** Think naturally: first is 1, second is 2, last is -1.
5. **Lock safety-critical data:** Use `fix` for configs and constants that should never mutate.

---

## 4. Congratulations! 🎓

You have completed the entire documentation for BoseLang! You now know everything needed to write fast, elegant, and modern programs.

Happy Coding with **BoseLang**! 🚀
