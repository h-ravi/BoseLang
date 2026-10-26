# 📚 Chapter 07: Lists & Maps (Collections)

In this chapter, you will learn how to store and organize collections of data using **Lists** and **Maps**, how **1-based indexing** works, how to slice collections, and how to use list and map methods.

---

## 1. What is a Collection?

So far, we stored single values in variables (like `age = 25`). But real-world applications handle groups of items:
- Shopping carts with dozens of items.
- User accounts with profiles, settings, and scores.

BoseLang provides two built-in collection types:
1. **Lists:** An ordered sequence of items `[ ... ]`.
2. **Maps:** Key-value mappings `{ ... }`.

---

## 2. Lists in BoseLang

Lists are created using square brackets `[ ... ]`:

```bose
fruits = ["Apple", "Mango", "Banana"]
numbers = [10, 20, 30, 40]
mixed = [1, "BoseLang", 3.14, true]
```

---

## 3. 🌟 The 1-Based Indexing Golden Rule 🌟

In real life, counting naturally starts at **1**:
- The **1st** item is item number 1.
- The **2nd** item is item number 2.
- Nobody points to the first item on a desk and calls it "Item Zero"!

> [!IMPORTANT]
> **In BoseLang, all list and string indexing starts at 1!**
> - Index `1` is the **first** element.
> - Index `2` is the **second** element.
> - Index `0` is **NOT allowed** and triggers a clear, protective runtime error.

```bose
fruits = ["Apple", "Mango", "Banana"]

out("1st element:", fruits[1])  /* Apple */
out("2nd element:", fruits[2])  /* Mango */
out("3rd element:", fruits[3])  /* Banana */
```

### ❌ What happens if you try index 0?
```bose
out(fruits[0])
/* Index Error: BoseLang uses 1-based indexing; index 0 is invalid.
   Hint: In BoseLang, counting starts at 1. Use 'list[1]' for the first item, or 'list[-1]' for the last item. */
```

---

## 4. Negative Indexing: Counting from the End

To access elements from the back of the list without calculating its length:
- `fruits[-1]` is the **last** item.
- `fruits[-2]` is the **second to last** item.

```bose
fruits = ["Apple", "Mango", "Banana"]

out("Last element:", fruits[-1])        /* Banana */
out("Second to last:", fruits[-2])      /* Mango */
```

---

## 5. Modifying Lists

### A. Updating an item:
```bose
fruits = ["Apple", "Mango", "Banana"]
fruits[1] = "Pineapple"

out(fruits)  /* ["Pineapple", "Mango", "Banana"] */
```

### B. Adding items: `.add(item)`
```bose
numbers = [1, 2]
numbers.add(3)

out(numbers)  /* [1, 2, 3] */
```

### C. Removing items by 1-based index: `.remove(index)`
```bose
items = ["Pen", "Pencil", "Eraser"]
items.remove(1)  /* Removes "Pen" */

out(items)  /* ["Pencil", "Eraser"] */
```

### D. Clearing all items: `.clear()`
```bose
items.clear()
out(items)  /* [] */
```

### E. Finding length: `len(list)`
```bose
fruits = ["Apple", "Mango", "Banana"]
out("Total fruits:", len(fruits))  /* 3 */
```

---

## 6. Slicing: Extracting Sub-Portions

Use range syntax `[start..end]` to extract items (both bounds inclusive):

```bose
scores = [10, 20, 30, 40, 50]

top_three = scores[1..3]
out(top_three)  /* [10, 20, 30] */
```

### Slicing Text:
Strings support the same 1-based indexing and slicing rules:
```bose
name = "BoseLang"
out(name[1..4])   /* "Bose" */
out(name[1])      /* "B" */
out(name[-1])     /* "g" */
```

---

## 7. Maps: Key-Value Dictionaries

Maps store pairs of `"key": value` using curly braces `{ ... }`:

```bose
user = {
    "name": "Subhash",
    "age": 25,
    "city": "Kolkata"
}
```

### A. Reading by Key:
```bose
out("Name:", user["name"])  /* Subhash */
out("Age:", user["age"])    /* 25 */
```

### B. Safe Missing Key Access:
In BoseLang, requesting a non-existent key does **not** crash your program. It safely returns **`Null`**:
```bose
out("Salary:", user["salary"])  /* Null */
```

### C. Map Keys vs. Positional Access (`index` / `idx`):
In BoseLang, bracket access `map[k]` is **always for Keys** (whether string or number). When you want to access or update by **1-based position**, use the built-in **`index(...)`** or its shorthand alias **`idx(...)`**:

```bose
user = {"name": "Subhash", "age": 25}

/* 1. Setting and getting by key (numbers as keys work cleanly): */
user[1] = 500
out("By key 1:", user[1])      /* 500 */
out("By key name:", user["name"]) /* Subhash */

/* 2. Positional reading via index(1) or idx(1): */
out("1st pair:", user[index(1)])   /* (name: Subhash) */
out("Last pair:", user[idx(-1)])   /* (1: 500) */

/* 3. Positional in-place value update: */
user[index(1)] = "Netaji"
out("Updated 1st pair:", user[idx(1)]) /* (name: Netaji) */

/* 4. Destructuring pair into key and value: */
k, v = user[idx(1)]
out("Key:", k, "Value:", v)        /* Key: name Value: Netaji */
```

### D. Map Methods: `.keys()` and `.values()`
```bose
out("Keys:", user.keys())      /* ["name", "age", "city"] */
out("Values:", user.values())  /* ["Subhash", 25, "Kolkata"] */
```

---

## 8. Looping Over Collections with `from`

### A. Over a List:
```bose
colors = ["Red", "Green", "Blue"]

loop color from colors {
    out("Color:", color)
}
```

### B. Over a Map (Direct Key & Value Destructuring):
```bose
profile = ("name": "Subhash", "role": "Developer")

loop key, val from profile {
    out("  {key} -> {val}")
}
```

---

## 9. Locking Collections with `fix` (Immutability)

Use `fix` to prevent lists or maps from being mutated:

```bose
fix config = ["production", 8080]

/* config.add("debug") ❌ Error: Fixed Error: Cannot modify fixed list */
/* config[1] = "dev"   ❌ Error: Fixed Error: Cannot modify fixed list */
```

---

## 10. Summary Checklist

- [x] Lists use `[ ... ]`, Maps use `{ ... }`.
- [x] **1-based Indexing:** `list[1]` is the first item!
- [x] Index `0` is invalid.
- [x] Negative indexing: `list[-1]` accesses the last item.
- [x] Slicing: `list[1..3]` extracts sublist inclusive.
- [x] Missing map keys return `Null` safely.
- [x] Loop with `from`: `loop item from list` and `loop k, v from map`.
- [x] Methods: `.add()`, `.remove()`, `.clear()`, `.keys()`, `.values()`.
- [x] Immutability with `fix`.

Next: Learn about built-in functions and error handling in **[Chapter 08: Built-ins & Errors](./08_builtins_and_errors.md)**!
