# ➕ Chapter 03: Operators, Math & Shorthands

In this chapter, you will learn how to do math, calculate values, use shortcut operators, swap variables instantly, and combine expressions in BoseLang.

---

## 1. Arithmetic Operators

BoseLang supports all common mathematical calculations:

| Operator | Name | Example | Result | Explanation |
| :---: | :--- | :---: | :---: | :--- |
| **`+`** | Addition | `20 + 7` | `27` | Adds two numbers together. |
| **`-`** | Subtraction | `20 - 7` | `13` | Subtracts right number from left. |
| **`*`** | Multiplication | `20 * 7` | `140` | Multiplies two numbers. |
| **`/`** | Exact Division | `20 / 7` | `2.8571...` | Divides and **always** returns a `point` decimal. |
| **`//`** | Integer Division | `20 // 7` | `2` | Divides and drops the decimal part (quotient). |
| **`%`** | Modulo (Remainder) | `20 % 7` | `6` | Returns the remainder after integer division. |
| **`**`** | Power (Exponent) | `2 ** 3` | `8` | 2 raised to the power of 3 ($2 \times 2 \times 2$). |
| **`-`** | Unary Minus | `-x` | `-5` | Reverses the sign of a number. |

### Example Code:
```bose
a = 20
b = 7

out("a + b =", a + b)    /* 27 */
out("a - b =", a - b)    /* 13 */
out("a * b =", a * b)    /* 140 */
out("a / b =", a / b)    /* 2.857142857142857 */
out("a // b =", a // b)  /* 2 */
out("a % b =", a % b)    /* 6 */
out("2 ** 3 =", 2 ** 3)  /* 8 */
```

> [!NOTE]
> **Exact Division (`/`) vs. Integer Division (`//`):**
> - Use `/` when you want precise decimals (e.g., sharing a pizza: `7 / 2 = 3.5`).
> - Use `//` when you only care about whole parts (e.g., full hours in 150 minutes: `150 // 60 = 2`).

---

## 2. Text and List Concatenation with `+`

The `+` operator is smart. When used with text, it joins sentences together:

```bose
first = "Hello, "
second = "World!"
greeting = first + second
out(greeting)  /* "Hello, World!" */
```

When used with lists, it merges them:
```bose
evens = [2, 4]
odds = [1, 3]
all_numbers = evens + odds
out(all_numbers)  /* [2, 4, 1, 3] */
```

---

## 3. Shorthand Assignment Operators

Instead of writing `score = score + 10`, you can use the compact shortcut:

```bose
score = 50

score += 10   /* Same as: score = score + 10  (Now 60) */
score -= 5    /* Same as: score = score - 5   (Now 55) */
score *= 2    /* Same as: score = score * 2   (Now 110) */
score //= 10  /* Same as: score = score // 10 (Now 11) */

out("Final Score:", score)  /* 11 */
```

---

## 4. Multiple Assignment & Swapping Values

In many traditional languages, if you want to swap the values of two variables `a` and `b`, you have to create an awkward third variable `temp`.

In BoseLang, you can assign multiple variables on a single line and **swap them instantly**:

### Swapping Two Variables:
```bose
a = 10
b = 20

/* Swap values in one clean step! */
a, b = b, a

out("a is now:", a)  /* 20 */
out("b is now:", b)  /* 10 */
```

### Rotating Three Variables:
```bose
x = 1
y = 2
z = 3

/* Rotate: x gets y's value, y gets z's, z gets x's */
x, y, z = y, z, x

out("x:", x, "y:", y, "z:", z)  /* x: 2 y: 3 z: 1 */
```

---

## 5. Chained Assignment (Setting Multiple Variables at Once)

If multiple variables start with the exact same value, you can chain them together:

```bose
p = q = r = 42

out("p =", p, "q =", q, "r =", r)
/* Output: p = 42 q = 42 r = 42 */
```

---

## 6. Parentheses for Control: Order of Operations

Just like in school algebra, BoseLang follows standard mathematical precedence:
- Power (`**`) runs first.
- Multiplication (`*`, `/`, `//`, `%`) runs second.
- Addition & Subtraction (`+`, `-`) run last.

Use parentheses `( ... )` whenever you want to change the order:

```bose
/* Without parentheses: 5 * 2 runs first */
val1 = 10 + 5 * 2
out(val1)  /* 10 + 10 = 20 */

/* With parentheses: 10 + 5 runs first */
val2 = (10 + 5) * 2
out(val2)  /* 15 * 2 = 30 */
```

---

## 7. Summary Checklist

- [x] Basic math: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- [x] `/` always gives a decimal `point`, `//` gives a whole `int`.
- [x] Use `+=`, `-=`, `*=`, etc. for quick updates.
- [x] Swap variables effortlessly: `a, b = b, a`.
- [x] Chained variables: `p = q = r = 42`.
- [x] Use `( ... )` to group calculations.

Next: Learn how your program can make smart choices in **[Chapter 04: Conditionals & Decisions](./04_conditionals_and_decisions.md)**!
