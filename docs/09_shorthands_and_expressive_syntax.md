# ⚡ Chapter 09: Shorthands & Expressive Syntax

In this chapter, you will discover BoseLang's built-in **Shorthands** — expressive, concise syntax patterns designed around the philosophy: **"Kam code mein best result"** (Write less, achieve more).

---

## 1. Chained Comparison (School Maths Shorthand)

In most traditional languages, checking whether a value lies within an interval forces you to write redundant boolean combinations like `(age >= 18 && age <= 60)`. 

In BoseLang, you write directly using natural mathematical inequalities:

```bose
/* 1. Age boundary check: */
when 18 <= age <= 60 {
    out("Working age bracket")
}

/* 2. Score limits: */
when 0 <= marks <= 100 {
    out("Valid marks")
}

/* 3. Strictly between thresholds: */
when min < value < max {
    out("Within threshold")
}

/* 4. Multi-variable equality: */
when a == b == c {
    out("All three values are equal")
}
```

---

## 2. Instant Variable Swapping & Rotation

Forget temporary variables! In BoseLang, you swap two or more variables on a single line:

### A. Two-Variable Swap:
```bose
a = 10
b = 20

a, b = b, a

out("a:", a)  /* 20 */
out("b:", b)  /* 10 */
```

### B. Three-Variable Rotation:
```bose
x = 1
y = 2
z = 3

x, y, z = y, z, x

out(x, y, z)  /* 2 3 1 */
```

---

## 3. Chained Assignment (Multi-Variable Initialization)

When initializing multiple variables to the exact same starting value:

```bose
x = y = z = 0
status = flag = "pending"

out("x, y, z:", x, y, z)  /* 0 0 0 */
```

---

## 4. Destructuring / Multiple Assignment

Assign multiple variables simultaneously from literals or function return values:

```bose
/* 1. Multiple literals */
name, age, city = "Subhash", 25, "Kolkata"

/* 2. Multiple function returns */
block get_user_info() {
    give 101, "Admin"
}

id, role = get_user_info()
out("ID:", id, "Role:", role)  /* ID: 101 Role: Admin */
```

---

## 5. `from` & `not from` Membership Shorthands

Instead of chaining multiple `or` conditions, use `from` and `not from`:

### A. List Membership:
```bose
/* Traditional: when role == "admin" or role == "manager" or role == "moderator" */
when role from ["admin", "manager", "moderator"] {
    out("Access granted!")
}
```

### B. Range Membership:
```bose
when score from 1..10 {
    out("Single-digit score")
}
```

### C. Negated Membership (`not from`):
```bose
when user not from ["guest", "banned"] {
    out("Verified active account")
}
```

---

## 6. Single-Line Guard Clauses & One-Liners

Write short conditions or small functions cleanly on a single line:

```bose
/* Guard clauses / Early exits */
when error == true { stop }
when count == 0 { give Null }

/* Concise helper block */
block square(n) { give n * n }

/* Short loop */
loop i from 1..5 { out(i) }
```

---

## 7. Compound Arithmetic Operators

Update variables in place without repeating the variable name:

```bose
a = 10

a += 5     /* a = a + 5  -> 15 */
a -= 2     /* a = a - 2  -> 13 */
a *= 3     /* a = a * 3  -> 39 */
a /= 2     /* a = a / 2  -> 19.5 (point) */
a //= 2    /* a = a // 2 -> 9.0 (integer division) */
a %= 2     /* a = a % 2  -> 1.0 */
a **= 2    /* a = a ** 2 -> 1.0 (power) */
```

---

## 8. String Interpolation Shorthand

Embed expressions directly inside `"..."` text using `{variable_name}` without messy `+` concatenation:

```bose
user = "Subhash"
score = 98.5

out("Hello {user}, your score is {score}/100!")
```

---

## 9. Empty Placeholder Body (No `pass` Keyword)

BoseLang does not require Python's `pass` keyword. Empty `{}` braces are valid and act as clean no-ops:

```bose
block future_implementation() {
}

when condition {
}
```

---

## 10. Complete Shorthands Summary Table

| Shorthand | Example | Meaning / Equivalent |
|---|---|---|
| **Chained comparison** | `18 <= age <= 60` | `age >= 18 and age <= 60` |
| **Instant Swap** | `a, b = b, a` | Values swapped without temp variable |
| **Chained assignment** | `x = y = z = 0` | All variables initialized to 0 |
| **Destructuring** | `a, b = get_pair()` | Unpacks multiple return values |
| **List membership** | `when item from list` | `item` exists in `list` |
| **Range membership** | `when x from 1..10` | `1 <= x <= 10` |
| **Negated membership** | `when x not from list` | `x` does not exist in `list` |
| **Guard clause** | `when err { stop }` | Single-line execution |
| **String template** | `"Hello {name}"` | `"Hello " + name` |
| **Compound math** | `x += 5` | `x = x + 5` |
| **Infinite loop** | `loop { ... }` | `loop true { ... }` |
| **Expressive branch** | `again when cond` | `again cond` |
| **Type cast (Roop A)** | `change a to point` | Casts `a` to `point` dynamically |
| **Type lock (Roop B)** | `change b to point = 99.5` | Casts and locks `b` to `point` |
| **Placeholder** | `{}` or `{ Null }` | No-op (no `pass` keyword needed) |
