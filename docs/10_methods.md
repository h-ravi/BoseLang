# 10. BoseLang Built-in Methods (Methods ki Poori Guide)

BoseLang me sabhi built-in methods **"Ek Kaam = Ek Hi Canonical Naam"** ke siddhant par design kiye gaye hain. Isse code padhne aur sikhne me koi confusion nahi hota.

---

## 📑 Methods Index

1. [Search & Location: `find`, `pos`](#1-search--location-find-pos)
2. [Text Transformations: `upper`, `lower`, `title`](#2-text-transformations-upper-lower-title)
3. [Whitespace Trimming: `trim`, `ltrim`, `rtrim`](#3-whitespace-trimming-trim-ltrim-rtrim)
4. [Splitting & Joining: `split`, `join`](#4-splitting--joining-split-join)
5. [Text Checking & Replace: `starts`, `ends`, `replace`](#5-text-checking--replace-starts-ends-replace)
6. [List & Collection Methods: `sort`, `reverse`, `pop`, `count`](#6-list--collection-methods-sort-reverse-pop-count)
7. [Basic Collection Ops: `add`, `remove`, `clear`, `keys`, `values`](#7-basic-collection-ops-add-remove-clear-keys-values)

---

## 1. Search & Location (`find`, `pos`)

BoseLang me search karne ke 2 alag aur clear methods hain:

### `.find(query)` $\rightarrow$ `bool`
- **Kaam:** Sirf yeh check karta hai ki kya query exist karti hai ya nahi.
- **Return Type:** Strictly `true` ya `false`.
- **Kyu Zaroori Hai:** BoseLang ke `when` condition me strictly `bool` chahiye hota hai, isliye `.find()` zero-error boolean deta hai.

```bose
/* Text me */
s = "Netaji Subhash Bose"
out(s.find("Subhash"))       /* true */
out(s.find("Gandhi"))        /* false */

/* List me */
nums = [10, 20, 30]
out(nums.find(20))           /* true */
out(nums.find(99))           /* false */

/* Map me */
user = {"name": "Bose", "age": 25}
out(user.find("name"))       /* true */
```

---

### `.pos(query)` $\rightarrow$ `Range` / `int` / `Null`
- **Kaam:** Query ki **1-based position ya range** nikalta hai. Agar na mile to `Null` deta hai.
- **Text (Multi-letter Substring):** 1-based `Range` (`start..end`) deta hai. Is Range se aap **direct slicing** kar sakte hain:
```bose
s = "subhash"
r = s.pos("bhas")
out(r)           /* 3..6 (Range) */
out(s[r])        /* "bhas" (Direct range slicing!) */
```
- **Text (Single Letter):** Single letter ke liye direct 1-based `int` deta hai:
```bose
p = s.pos("b")
out(p)           /* 3 */
out(s[p])        /* "b" */
```
- **List:** Item ka 1-based index deta hai:
```bose
nums = [10, 20, 30]
i = nums.pos(30)
out(i)           /* 3 */
out(nums[i])     /* 30 */
```
- **Map:** Entry ki 1-based insertion position deta hai:
```bose
user = {"name": "Bose", "year": 1942}
pos = user.pos("year")
out(pos)                 /* 2 */
out(user[index(pos)])    /* ("year": 1942) */
```

---

## 2. Text Transformations (`upper`, `lower`, `title`)

### `.upper()` $\rightarrow$ `Text`
Poore text ko uppercase (bade aksharon) me badalta hai.
```bose
"bose".upper()               /* "BOSE" */
```

### `.lower()` $\rightarrow$ `Text`
Poore text ko lowercase (chhote aksharon) me badalta hai.
```bose
"BOSE".lower()               /* "bose" */
```

### `.title()` $\rightarrow$ `Text`
Har word ka pehla letter capital banata hai.
```bose
"subhash chandra bose".title()  /* "Subhash Chandra Bose" */
"delhi-chalo".title()           /* "Delhi-Chalo" */
```

---

## 3. Whitespace Trimming (`trim`, `ltrim`, `rtrim`)

Faltu space hatane ke liye 3 saaf aur seedhe methods hain:

| Method | Kaam | Example | Result |
|---|---|---|---|
| **`.trim()`** | Dono side se spaces hatata hai | `"   bose   ".trim()` | `"bose"` |
| **`.ltrim()`** | Sirf Left (shuruat) se spaces hatata hai | `"   bose   ".ltrim()` | `"bose   "` |
| **`.rtrim()`** | Sirf Right (aakhir) se spaces hatata hai | `"   bose   ".rtrim()` | `"   bose"` |

---

## 4. Splitting & Joining (`split`, `join`)

### `.split([delim])` $\rightarrow$ `List`
Text ko todkar List banata hai:
1. **Bina argument:** Whitespace (space/tab) se todta hai.
   ```bose
   "Delhi Chalo Now".split()     /* ["Delhi", "Chalo", "Now"] */
   ```
2. **Delimiter ke sath:**
   ```bose
   "apple,banana,mango".split(",") /* ["apple", "banana", "mango"] */
   ```
3. **Empty string `""` ke sath:** Har single character alag karta hai.
   ```bose
   "Bose".split("")              /* ["B", "o", "s", "e"] */
   ```

### `.join(delim)` $\rightarrow$ `Text`
List ke saare items ko ek separator ke sath jodkar Text banata hai.
BoseLang me yeh **dono tarike** se natural tarike se chalta hai:

1. **List-first style:**
   ```bose
   items = ["apple", "banana", "mango"]
   out(items.join(" - "))        /* "apple - banana - mango" */
   ```
2. **Delimiter-first style (Path / URL me natural):**
   ```bose
   folders = ["usr", "local", "bin"]
   out("/".join(folders))        /* "usr/local/bin" */
   ```

---

## 5. Text Checking & Replace (`starts`, `ends`, `replace`)

### `.starts(prefix)` $\rightarrow$ `bool`
Check karta hai text is prefix se start hota hai ya nahi.
```bose
"Netaji Subhash".starts("Netaji")  /* true */
```

### `.ends(suffix)` $\rightarrow$ `bool`
Check karta hai text is suffix par end hota hai ya nahi.
```bose
"Subhash Bose".ends("Bose")        /* true */
```

### `.replace(from, to, [limit])` $\rightarrow$ `Text`
Kisi word ya letter ko doosre se replace karta hai:
```bose
s = "Give me blood, and I will give you freedom"
out(s.replace("give", "offer"))     /* case-sensitive full replace */
out(s.replace(" ", "_", 2))         /* sirf pehle 2 spaces replace honge */
```

---

## 6. List & Collection Methods (`sort`, `reverse`, `pop`, `count`)

### `.sort()`
List ko in-place ascending order me sort karta hai:
```bose
nums = [40, 10, 50, 20, 30]
nums.sort()
out(nums)                    /* [10, 20, 30, 40, 50] */
```
*(Fix list pe error dega).*

### `.reverse()`
- **List par:** In-place list ke elements ko ulta kar deta hai.
  ```bose
  nums = [1, 2, 3]
  nums.reverse()
  out(nums)                  /* [3, 2, 1] */
  ```
- **Text par:** Naya reversed text return karta hai:
  ```bose
  out("Netaji".reverse())     /* "ijateN" */
  ```

### `.pop([index])`
- **Bina argument:** Aakhiri element remove karke return karta hai.
  ```bose
  l = [10, 20, 30]
  out(l.pop())               /* 30 */
  out(l)                     /* [10, 20] */
  ```
- **1-based Index ke sath:** Us position ka element remove karke return karta hai.
  ```bose
  out(l.pop(1))              /* 10 */
  out(l)                     /* [20] */
  ```

### `.count(needle)` $\rightarrow$ `int`
Occurrence count karta hai:
```bose
/* List me */
[1, 2, 2, 3, 2].count(2)     /* 3 */

/* Text me */
"abracadabra".count("a")     /* 5 */
```

---

## 7. Basic Collection Ops (`add`, `remove`, `clear`, `keys`, `values`)

- `list.add(item)`: List ke aakhir me naya item jodta hai. (Alias: `list.append(item)`).
- `map.add(key, val)`: Map me key-value jodta hai.
- `list.remove(1)`: 1-based index se item delete karta hai.
- `map.remove("key")`: Key delete karta hai.
- `coll.clear()`: Saare items delete karta hai.
- `map.keys()`: Saari keys ki List deta hai.
- `map.values()`: Saari values ki List deta hai.

---

## 💡 Compiler Guidance & Helpful Hints

Agar koi developer purani ya doosri language ki aadat se yeh aliases type karta hai, to BoseLang ka compiler crash nahi hota, balki turant sahi hint deta hai:

| Agar aapne likha | Compiler ka Hint |
|---|---|
| `.has(x)` ya `.contains(x)` | `Hint: In BoseLang, use '.find(...)' to check if an item exists.` |
| `.position(x)` | `Hint: In BoseLang, use '.pos(...)' to get the 1-based index or range.` |
| `.clean()` | `Hint: In BoseLang, use '.trim()', '.ltrim()', or '.rtrim()'.` |
| `.starts_with(x)` | `Hint: In BoseLang, use concise '.starts(...)'.` |
| `.ends_with(x)` | `Hint: In BoseLang, use concise '.ends(...)'.` |
| `.push(x)` | `Hint: In BoseLang, use '.add(...)'.` |
