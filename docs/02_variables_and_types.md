# 📦 Chapter 02: Variables & Data Types

In this chapter, you will learn how to store information, what types of data exist in BoseLang, how to convert between types, and how to lock variables so nobody can accidentally change them.

---

## 1. What is a Variable? (The Labeled Box Analogy)

Imagine you have cardboard boxes in your room:
- On one box, you write the label **`player_name`** and place the text `"Subhash"` inside it.
- On another box, you write the label **`score`** and place the number `100` inside it.

In computer programming, a **variable** is simply a labeled storage box in memory where you keep values.

```bose
/* Storing values in variables */
player_name = "Subhash"
score = 100

out("Player:", player_name)
out("Score:", score)
```

**Output:**
```text
Player: Subhash
Score: 100
```

---

## 2. The 5 Core Data Types in BoseLang

Every value in BoseLang belongs to a specific type:

| Type Name | What it Represents | Examples |
| :---: | :--- | :--- |
| **`int`** | Whole numbers (integers), positive or negative. | `1`, `42`, `-10`, `0` |
| **`point`** | Decimal numbers (floating-point numbers). | `3.14`, `0.5`, `99.99` |
| **`text`** | Words, sentences, characters enclosed in `"..."`. | `"Hello"`, `"BoseLang"`, `"123"` |
| **`bool`** | Logical truth values: either `true` or `false`. | `true`, `false` |
| **`Null`** | Represents the absence of a value (empty/nothing). | `Null` |

---

## 3. The 3 Variable Forms in BoseLang

In BoseLang, every variable belongs to one of **three distinct forms**:

| Variable Form | Declaration Example | Can Value Change? (`a = 20`) | Can Type Change? (`a = "text"`) |
|---|---|:---:|:---:|
| **1. Dynamic** | `a = 10` | ✅ Yes | ✅ Yes (automatic) |
| **2. Type-Locked** | `int a = 10` | ✅ Yes (if same type) | ❌ No (requires `change a to text`) |
| **3. Fixed** | `fix a = 10` | ❌ No (immutable) | ❌ No (immutable) |

---

### A. Dynamic (Quick & Flexible)
You do not specify the type; BoseLang automatically understands it and allows both value and type to change dynamically:
```bose
a = 10               /* Initially an int */
a = 20               /* Value updated: 20 (int) */
a = 10.5             /* Type dynamically changed to point */
a = "Subhash"        /* Type dynamically changed to text */
```

### B. Explicitly Typed & Type Locked (Clear & Strict)
You can prefix the variable name with its type. This locks the variable to that type for its entire lifetime:
```bose
int student_id = 101
point temperature = 98.6
text school = "Bose Academy"
bool is_passed = true
```

#### 🔒 Type Locking & Safety Rules:
When you declare `int a = 10`:
1. `a = 20` is **completely valid** because 20 is also an `int`. But `a` does NOT become dynamic — its type remains strictly locked to `int`!
2. `a = "Subhash"` is **strictly rejected** with a compile-time `Type Error`!
3. If you want to change its type later, you must explicitly give consent using `change a to text`.

---

## 4. Checking a Variable's Type: `type(...)`

You can inspect the type of any value using the built-in `type()` function:

```bose
out(type(42))         /* "int" */
out(type(3.14))       /* "point" */
out(type("Hello"))    /* "text" */
out(type(true))       /* "bool" */
out(type(Null))       /* "Null" */
```

---

## 5. Changing Data Types: The `change` Statement

When you need to convert an existing variable to another type, BoseLang provides the **`change`** statement with two intuitive forms:

### Form A: Type Conversion (Variable Becomes Dynamic)
Converts the existing value in-place, and frees the variable to hold dynamic values:
```bose
int a = 10
change a to point

out(a)        /* 10.0 */
out(type(a))  /* "point" */

a = "Now dynamic!"   /* ✅ Allowed! */
```

### Form B: Type Conversion with New Value (Type Locked)
Sets a new value and strictly locks the variable to the new target type:
```bose
int b = 10
change b to point = 99.5

out(b)        /* 99.5 */
out(type(b))  /* "point" */

/* b is now locked to point: */
b = "hello"   /* ❌ Type Error: Cannot assign 'text' to variable typed as 'point' */
b = 20        /* ✅ Auto-converted to 20.0 */
```

---

## 6. Variable Scoping & Shadowing

BoseLang uses clean lexical block scoping:
- **Block Isolation:** Any variable declared inside `{}` (such as within a `when` block, `loop`, or function) is isolated to that block and automatically cleaned up when the block finishes.
- **No Scope Leaks:** Trying to read a loop or conditional's inner variable from the outside produces a clean `Name Error: Variable '<name>' is not defined`.
- **Reassignment (`total = total + i`):** Plain assignments find and update the nearest outer variable, allowing loops to accumulate totals and counters.
- **Shadowing (`int x = 20`):** Explicitly declaring a typed variable inside a block shadows the outer variable. The inner code sees the new value, while the outer variable remains completely untouched!

---

## 7. String Interpolation (Embedding Variables in Text)

Instead of stitching strings together with `+`, BoseLang allows you to put `{variable_name}` directly inside `"..."` text:

```bose
user = "Aman"
rank = 1
points = 98.5

/* Clean, readable sentence */
out("Congratulations {user}! You are Rank #{rank} with {points} points.")
```

**Output:**
```text
Congratulations Aman! You are Rank #1 with 98.5 points.
```

Any variable inside `{...}` is automatically converted to text and inserted into the sentence!

---

## 8. Locking Variables: The `fix` Keyword (Immutability)

What if you have a variable that should **never** be changed or modified (like the speed of light, value of Pi, or a sensitive configuration list)?

Use the **`fix`** keyword:

```bose
/* A fixed constant */
fix PI = 3.14159
fix MAX_USERS = 500
```

Once a variable is marked as `fix`:
1. It **cannot** be reassigned to a new value (`PI = 3.0` ❌ triggers compile-time `Fixed Error`).
2. If it is a list or map, items **cannot** be added, modified, or removed!

### Example: Protecting a List
```bose
fix allowed_roles = ["admin", "moderator"]

/* Trying to add another role will cause an error! */
allowed_roles.add("hacker")  /* ❌ ERROR: Fixed Error: Cannot modify fixed list */
```

> [!TIP]
> Use `fix` whenever you want to protect your data from accidental changes. It is a powerful safety feature!

---

## 9. Summary Checklist

- [x] A variable is a named storage box for data.
- [x] The 5 core types are `int`, `point`, `text`, `bool`, and `Null`.
- [x] You can write dynamic `x = 10` or type-locked `int x = 10`.
- [x] Use `type(x)` to inspect what type a value is.
- [x] Use `change x to <type>` to convert types (Form A: dynamic, Form B: type-locked).
- [x] Inner blocks isolate variables; outer variables cannot be leaked.
- [x] Use `"{var}"` inside strings to cleanly insert variables.
- [x] Use `fix` to lock a variable or collection permanently.

Next: Learn arithmetic, calculations, and shortcut operators in **[Chapter 03: Operators & Math](./03_operators_and_math.md)**!
