# 🔁 Chapter 05: Loops & Ranges

In this chapter, you will learn how to repeat actions without duplicate code using the unified **`loop`** statement, how to count using smart **Ranges**, and how to control flow using **`stop`** and **`skip`**.

---

## 1. Unified `loop` Keyword

BoseLang does not force you to remember separate `for` and `while` keywords. A single keyword handles both:

| Loop Type | Syntax | Traditional Equivalent | Use Case |
| :---: | :--- | :---: | :--- |
| **Condition-Based** | `loop condition { ... }` | `while` loop | Repeats while condition remains `true`. |
| **Range-Based** | `loop i from 1..10 { ... }` | `for i in range` | Iterates through number sequences. |
| **Collection-Based** | `loop item from list { ... }` | `for-each` | Iterates over elements of a list, map, or string. |

---

## 2. Condition-Based Loops (`while` style)

A condition loop runs as long as its condition is `true`:

```bose
count = 1

loop count <= 3 {
    out("Current count:", count)
    count += 1
}

out("Loop finished!")
```

**Output:**
```text
Current count: 1
Current count: 2
Current count: 3
Loop finished!
```

### Infinite Loops: `loop { ... }` or `loop true { ... }`

You can write infinite loops using the concise shorthand `loop { ... }` or explicit `loop true { ... }`:

```bose
/* Infinite loop with clean 'loop { ... }' shorthand */
loop {
    cmd = in("Enter command ('exit' to quit): ")
    when cmd == "exit" {
        stop
    }
    out("Echo:", cmd)
}
```

---

## 3. Ranges in BoseLang: Counting Made Beautiful

A **range** represents a sequence of numbers from start to end using `..`.

### A. Fully Inclusive Range (`start..end`)
Unlike Python where the last number is omitted, in BoseLang ranges are **fully inclusive**:

```bose
/* Counts 1, 2, 3, 4, 5 */
loop i from 1..5 {
    out("Step:", i)
}
```

### B. Automatic Countdown (`start..end`)
When `start > end`, BoseLang automatically counts downwards:

```bose
/* Counts 5, 4, 3, 2, 1 */
loop i from 5..1 {
    out("Countdown:", i)
}
```

### C. Custom Step (`start..end..step`)
Specify step jump as the 3rd value:

```bose
/* Starts at 1, increments by 2 up to 9 */
loop i from 1..10..2 {
    out("Odd number:", i)  /* 1, 3, 5, 7, 9 */
}

/* Reverse step */
loop i from 10..0..2 {
    out("Even countdown:", i)  /* 10, 8, 6, 4, 2, 0 */
}
```

### D. Using Variables in Ranges:
```bose
first = 1
last = 50
jump = 10

loop i from first..last..jump {
    out("i =", i)  /* 1, 11, 21, 31, 41 */
}
```

### E. Open-Ended Ranges (`start..` and `..end`):
BoseLang supports natural open ranges for slicing and file streaming:
* `2..` : Starts at 2 and continues forward to the end (EOF).
* `..10`: Starts at 1 and stops at 10.

```bose
/* Streaming from line 2 to end of file (skipping header) */
loop line from read_stream("data.csv", 2..) {
    out(line)
}
```

---

## 4. Collection-Based Loops

Iterate over any collection using `from`:

### A. Over a List:
```bose
fruits = ["Apple", "Mango", "Banana"]

loop fruit from fruits {
    out("Enjoying:", fruit)
}
```

### B. Over a Map (Direct Key & Value Destructuring!):
```bose
scores = ("Math": 95, "Physics": 90, "English": 88)

loop subject, mark from scores {
    out("{subject} -> {mark}/100")
}
```

### C. Over Letters in Text:
```bose
word = "Bose"

loop char from word {
    out("Letter:", char)
}
```

### D. Over a File Stream (Memory-Safe Lazy Streaming):
For large files (CSVs, logs, big text files), stream line-by-line with constant ~8 KB memory:
```bose
loop line from read_stream("big_data.csv") {
    out("Streamed line:", line)
}
```

---

## 5. Loop Control: `stop` and `skip`

| Keyword | Traditional Name | Action |
| :---: | :---: | :--- |
| **`stop`** | `break` | Immediately terminates the loop and exits. |
| **`skip`** | `continue` | Skips remaining statements in the current round and proceeds to the next iteration. |

### `stop` Example:
```bose
loop i from 1..10 {
    when i == 4 {
        out("Target reached, stopping!")
        stop
    }
    out("Number:", i)
}
/* Prints 1, 2, 3 and stops */
```

### `skip` Example:
```bose
loop i from 1..5 {
    when i == 3 {
        skip  /* Skips printing 3 */
    }
    out("Running:", i)
}
/* Prints 1, 2, 4, 5 */
```

---

## 6. Nested Loops & Innermost Control

In nested loops, `stop` and `skip` apply strictly to the **innermost** loop:

```bose
loop row from 1..3 {
    loop col from 1..3 {
        when col == 2 {
            stop  /* Only inner col loop stops */
        }
        out("Row:", row, "Col:", col)
    }
}
```

---

## 7. Scope & Variable Isolation

1. **Loop variable isolation:** The iteration variable `i` in `loop i from 1..3` is local to the loop and will **never** overwrite an outer variable named `i`:
   ```bose
   i = 999
   loop i from 1..3 {
       out("Inside:", i)  /* 1, 2, 3 */
   }
   out("Outside:", i)    /* 999 (Untouched!) */
   ```

2. **Loop internals do not leak:** Variables declared inside a loop block stay inside:
   ```bose
   loop i from 1..3 {
       temp = i * 10
   }
   /* out(temp) ❌ Undefined Variable Error */
   ```

---

## 8. Empty Placeholder Bodies (No `pass` Needed)

In BoseLang, empty `{}` or `{ Null }` naturally acts as a no-op placeholder:

```bose
loop i from 1..100 {
}
```

---

## 9. Summary Checklist

- [x] Unified `loop` syntax: condition-based, range-based, and collection-based.
- [x] Range inclusive: `1..5` includes `5`.
- [x] Countdown ranges: `5..1` automatically counts down.
- [x] Stepped ranges: `1..10..2`.
- [x] Collection iteration: `loop item from list`.
- [x] Map destructuring: `loop k, v from map`.
- [x] `stop` terminates loop; `skip` advances to next iteration.
- [x] Variables inside loop blocks do not leak into outer code.

Next: Learn how to write reusable functions with **[Chapter 06: Blocks & Functions](./06_blocks_and_functions.md)**!
