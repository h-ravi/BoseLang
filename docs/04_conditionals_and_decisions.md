# 🔀 Chapter 04: Conditionals & Decisions

In this chapter, you will learn how to make your program think and decide what to do using BoseLang's original conditional keywords: **`when`**, **`again`**, and **`otherwise`**.

---

## 1. Overview of Conditional Keywords

Unlike older languages that use confusing abbreviations like `elif` or `elsif`, BoseLang uses plain, expressive English words:

| Keyword | Role | Meaning |
| :---: | :--- | :--- |
| **`when`** | Primary Check | Runs its block if the condition evaluates to `true`. |
| **`again`** *(or `again when`)* | Alternative Check | Checks the next condition if previous checks were `false`. |
| **`otherwise`** | Default Fallback | Runs if all previous `when` and `again` checks were `false`. |

---

## 2. Basic `when` Statement

In everyday life, decisions are simple:
- *"When it rains, take an umbrella."*
- *"When the battery is low, plug in the charger."*

```bose
score = 85

when score >= 50 {
    out("Congratulations! You passed the test.")
}
```

The code inside `{ ... }` runs **only** if the condition (`score >= 50`) is `true`.

---

## 3. Two-Way Decisions: `when` and `otherwise`

When you want to do one thing on `true` and another on `false`:

```bose
age = 15

when age >= 18 {
    out("Eligible to vote!")
} otherwise {
    out("Minor — cannot vote yet.")
}
```

---

## 4. Multi-Condition Chains: `when` → `again` → `otherwise`

When there are multiple options (e.g., student grades):

```bose
score = 78

when score >= 90 {
    out("Grade: A (Outstanding)")
} again score >= 75 {
    out("Grade: B (Very Good)")
} again when score >= 50 {
    out("Grade: C (Passed)")
} otherwise {
    out("Grade: F (Needs Improvement)")
}
```

> [!NOTE]
> **Both `again` and `again when` are valid!**
> You can write the concise form `again score >= 75 { ... }` or the explicit English form `again when score >= 75 { ... }`. Both compile to identical high-speed bytecode.

### Execution Flow:
1. `when` is evaluated first.
2. If `false`, the first `again` is evaluated.
3. **First Match Wins:** The very first condition that evaluates to `true` runs its block, and the rest of the chain is immediately skipped!
4. If all conditions evaluate to `false`, `otherwise` runs.

---

## 5. Comparison Operators

| Operator | Meaning | Example | Result |
| :---: | :--- | :---: | :---: |
| **`==`** | Equal to | `5 == 5` | `true` |
| **`!=`** | Not equal to | `5 != 3` | `true` |
| **`<`** | Less than | `3 < 5` | `true` |
| **`>`** | Greater than | `5 > 10` | `false` |
| **`<=`** | Less than or equal to | `5 <= 5` | `true` |
| **`>=`** | Greater than or equal to | `10 >= 7` | `true` |

> [!WARNING]
> Assignment (`=`) is strictly **banned** inside conditions:
> ```bose
> when x = 5 { }  /* ❌ Syntax Error: Did you mean '=='? */
> ```

---

## 6. Chained Comparisons: School Maths Notation 🌟

In languages like C or Java, checking if a number lies between 18 and 60 requires writing:
`if (age >= 18 && age <= 60)` (repetitive and unnatural).

In BoseLang, you can write it **exactly as written in a mathematics book**:

```bose
age = 30

when 18 <= age <= 60 {
    out("Working age group: 18 <= 30 <= 60 is true!")
}
```

You can chain multiple inequalities:
```bose
min = 10
val = 25
max = 50

when min < val < max {
    out("Value is strictly between min and max!")
}

/* Equality chaining: */
when a == b == c {
    out("All three variables are equal!")
}
```

---

## 7. Logical Operators: `and`, `or`, `not`

Combine multiple conditions with plain English words:

### A. `and` (Both must be true)
```bose
has_ticket = true
has_id = true

when has_ticket and has_id {
    out("Welcome inside!")
}
```

### B. `or` (At least one must be true)
```bose
has_cash = false
has_upi = true

when has_cash or has_upi {
    out("Payment accepted!")
}
```

### C. `not` (Inverts boolean value)
```bose
is_banned = false

when not is_banned {
    out("Access permitted.")
}
```

> [!NOTE]
> BoseLang uses **short-circuit evaluation**:
> - In `a and b`: if `a` is `false`, `b` is never evaluated.
> - In `a or b`: if `a` is `true`, `b` is never evaluated.

---

## 8. Membership Testing: `from` and `not from`

To check if an item belongs to a list or range:

### A. Checking List Membership:
```bose
role = "editor"

when role from ["admin", "editor", "moderator"] {
    out("Access granted!")
}
```

### B. Checking Range Membership:
```bose
score = 7

when score from 1..10 {
    out("Score is a single digit between 1 and 10!")
}
```

### C. Negated Membership (`not from`):
```bose
guest = "hacker"

when guest not from ["admin", "moderator"] {
    out("Access denied!")
}
```

---

## 9. Single-Line Guard Clauses

For short checks or early returns, write `{}` on a single line:

```bose
when error == true { stop }
when count == 0 { give Null }
when role == "admin" { out("Welcome Admin") }
```

---

## 10. Strict Boolean Rule

Conditions in BoseLang must evaluate to a strict `bool` (`true` or `false`):
```bose
when 1 { }       /* ❌ Type Error: Condition must be bool, found int */
when "text" { }  /* ❌ Type Error: Condition must be bool, found text */
```
This protects you from accidental bugs and unexpected behavior!

---

## 11. Summary Checklist

- [x] Use `when` for the initial check.
- [x] Use `again` for additional alternative conditions.
- [x] Use `otherwise` as the final fallback.
- [x] Chained comparisons: `18 <= age <= 60`.
- [x] Logical operators: `and`, `or`, `not`.
- [x] Membership: `when item from collection` and `when item not from collection`.
- [x] Single-line guard clauses: `when err { stop }`.
- [x] Conditions must evaluate strictly to `true` or `false`.

Next: Learn how to repeat code with **[Chapter 05: Loops & Ranges](./05_loops_and_ranges.md)**!
