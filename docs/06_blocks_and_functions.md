# 🧱 Chapter 06: Blocks & Functions

In this chapter, you will learn how to organize your code into reusable recipes called **Blocks**, how to return values using **`give`**, how to unpack multiple return values, and how **`block auto`** works.

---

## 1. What is a Block? (The Recipe Analogy)

Instead of rewriting the same 10 lines of code every time you need a task performed, you create a named **`block`**:

```bose
/* Defining a block */
block greet(name) {
    out("Namaste,", name)
}

/* Calling the block */
greet("Subhash")
greet("Priya")
```

BoseLang avoids unnecessary keywords like `function`, `func`, `def`, or `fn`. A single clear keyword is used: **`block`**.

---

## 2. Returning Values: The `give` Keyword

When a block computes a result and sends it back to the caller, it uses **`give`**:

```bose
block add(a, b) {
    give a + b
}

ans = add(15, 25)
out("15 + 25 =", ans)  /* 40 */
```

### Early Exit with Empty `give`:
An empty `give` immediately exits the function and returns `Null`:

```bose
block check_age(age) {
    when age < 18 {
        out("Underage!")
        give  /* Exits early, returning Null */
    }
    out("Access granted.")
}
```

### Default Return:
If a block completes its execution without hitting an explicit `give`, it automatically returns **`Null`**.

---

## 3. Multiple Return Values & Destructuring 🌟

A block can return multiple values simultaneously by separating them with commas after `give`:

```bose
block calculate_stats(a, b) {
    total = a + b
    diff = a - b
    give total, diff
}

/* Unpack multiple returns in a single line! */
sum_val, diff_val = calculate_stats(20, 5)

out("Sum:", sum_val)    /* 25 */
out("Diff:", diff_val)  /* 15 */
```

---

## 4. Default Parameters (Trailing Only)

Parameters can have default values. If the caller omits an argument, the default is used:

```bose
block send_message(recipient, prefix = "Info", urgent = false) {
    out("[{prefix}] To: {recipient} (Urgent: {urgent})")
}

send_message("Aman")                      /* Uses defaults */
send_message("Boss", "Urgent", true)      /* Overrides defaults */
```

> [!NOTE]
> Parameters with default values must be placed at the end (trailing) of the parameter list.

---

## 5. Order-Independent Definitions (Define Anywhere!)

In BoseLang, blocks are registered before top-level execution begins. You can call a block at the top of your script even if its definition is at the very bottom:

```bose
/* Call before definition */
start_engine()

block start_engine() {
    out("Engine initialized successfully!")
}
```

---

## 6. `block auto`: Automatic Entry Points 🚀

A `block auto` is automatically executed by the runtime as soon as your script loads:

```bose
block auto init_database() {
    out("1. Database connected.")
}

block auto launch_server() {
    out("2. Server running on port 8080.")
}
```

**Output:**
```text
1. Database connected.
2. Server running on port 8080.
```

### Rules for `block auto`:
1. Executed in **FIFO (top-to-bottom)** declaration order.
2. Cannot accept parameters (zero parameters).
3. Return values are discarded by the runtime.

---

## 7. Dynamic Parameters

Parameters in BoseLang are dynamic:
```bose
block square(x) {
    give x * x
}

out(square(5))     /* 25 (works with int) */
out(square(2.5))   /* 6.25 (works with point) */
```

---

## 8. Recursion

Blocks can call themselves to solve recursive mathematical problems cleanly:

```bose
block fibonacci(n) {
    when n <= 1 {
        give n
    }
    give fibonacci(n - 1) + fibonacci(n - 2)
}

out("fib(10) =", fibonacci(10))  /* 55 */
```

---

## 9. Empty Block Placeholder (No `pass`)

To leave a function body empty while sketching code:
```bose
block feature_in_progress() {
}
```

---

## 10. Summary Checklist

- [x] Defined with `block name(params) { ... }`.
- [x] Returned values with `give`.
- [x] Empty `give` returns `Null`.
- [x] Multiple returns: `give a, b` destructured with `x, y = fn()`.
- [x] Default parameters at the end: `block test(a, b = 10)`.
- [x] Functions can be called before their definitions.
- [x] `block auto` executes automatically on startup.
- [x] Recursion is supported and fast.

Next: Learn how to manage collections of data in **[Chapter 07: Lists & Maps](./07_collections_lists_and_maps.md)**!
