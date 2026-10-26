# 14. Level 6 Math Module Guide (`math`, Capability Security & Bose Specials)

Status: **Certified Level 6 Architecture**

BoseLang Level 6 introduces a modular, zero-dependency, ultra-fast **Math Module**. It is designed with pure modular architecture (`src/module/math/`), ensuring the core VM dispatch loop remains lightweight and blazing fast.

Furthermore, BoseLang introduces **Capability-Based Security & Power Transfer**: you can grant full math powers or restrict access by category or individual function.

---

## 1. Getting Started: Accessing Math

### 1.1 Full Access (`fix m = math`)
To obtain full, unrestricted math capabilities:
```bose
fix m = math

out(m.sqrt(16))     // 4
out(m.pi)           // 3.141592653589793
out(m.factorial(5)) // 120
```

### 1.2 Capability-Based Security & Power Transfer
In production or sandbox environments, you can limit which math operations a function or script can perform:

#### By Category:
```bose
/* Grants only basic category: abs, min, max, round, floor, ceil, clamp, sign */
fix m_basic = math(basic)

out(m_basic.abs(-50))          // 50
// m_basic.sqrt(25)            // Security Error: Capability 'sqrt' is not granted!
```

#### By Specific Function Names:
```bose
/* Grants only min, max, and sqrt */
fix m_safe = math(min, max, sqrt)

out(m_safe.sqrt(144))          // 12
out(m_safe.min(10, 5, 20))      // 5
// m_safe.pow(2, 8)            // Security Error: Capability 'pow' is not granted!
```

#### Safe Power Transfer to Functions:
```bose
block calculate_discount(m_tool, original_price, discount_pct) {
    savings = m_tool.percent_of(discount_pct, original_price)
    give original_price - savings
}

/* Grant only the 'percent_of' capability */
fix m_fin = math(percent_of)
out(calculate_discount(m_fin, 2500, 20)) // 2000
```

---

## 2. Complete Functions Reference

The math engine contains 40+ comprehensive functions divided across 6 clean categories:

### 2.1 Category: `basic`
| Function | Description | Example |
| :--- | :--- | :--- |
| `m.abs(x)` | Absolute value | `m.abs(-42)` -> `42` |
| `m.sign(x)` | Returns `-1`, `0`, or `1` | `m.sign(-15)` -> `-1` |
| `m.min(a, b, ...)` | Minimum value (supports list or varargs) | `m.min(10, 5, 20)` -> `5` |
| `m.max(a, b, ...)` | Maximum value (supports list or varargs) | `m.max(10, 5, 20)` -> `20` |
| `m.round(x)` | Rounds to nearest integer | `m.round(3.7)` -> `4` |
| `m.floor(x)` | Rounds down towards negative infinity | `m.floor(3.7)` -> `3` |
| `m.ceil(x)` | Rounds up towards positive infinity | `m.ceil(3.2)` -> `4` |
| `m.clamp(x, min, max)` | Clamps `x` within `[min, max]` | `m.clamp(15, 0, 10)` -> `10` |

---

### 2.2 Category: `power`
| Function | Description | Example |
| :--- | :--- | :--- |
| `m.sqrt(x)` | Square root | `m.sqrt(16)` -> `4` |
| `m.cbrt(x)` | Cube root | `m.cbrt(27)` -> `3` |
| `m.root(x, n)` | $n$-th root of $x$ | `m.root(81, 4)` -> `3` |
| `m.pow(base, exp)` | Power ($x^y$) | `m.pow(2, 8)` -> `256` |
| `m.log(x, [base])` | Natural log ($\ln x$) or custom base log | `m.log(100, 10)` -> `2.0` |
| `m.log10(x)` | Common base 10 log | `m.log10(1000)` -> `3.0` |
| `m.log2(x)` | Binary base 2 log | `m.log2(64)` -> `6.0` |
| `m.exp(x)` | Exponential ($e^x$) | `m.exp(1)` -> `2.71828...` |

---

### 2.3 Category: `theory` (Number Theory & Combinatorics)
| Function | Description | Example |
| :--- | :--- | :--- |
| `m.gcd(a, b)` | Greatest Common Divisor | `m.gcd(48, 18)` -> `6` |
| `m.lcm(a, b)` | Least Common Multiple | `m.lcm(12, 18)` -> `36` |
| `m.factorial(n)` | Factorial ($n!$) | `m.factorial(5)` -> `120` |
| `m.combinations(n, r)` | Combinations ($^nC_r$) | `m.combinations(5, 2)` -> `10` |
| `m.permutations(n, r)` | Permutations ($^nP_r$) | `m.permutations(5, 2)` -> `20` |
| `m.is_prime(n)` | Primality test | `m.is_prime(17)` -> `true` |
| `m.factors(n)` | Returns list of all divisors | `m.factors(28)` -> `[1, 2, 4, 7, 14, 28]` |
| `m.primes(limit)` | Returns list of primes up to `limit` | `m.primes(20)` -> `[2, 3, 5, 7, 11, 13, 17, 19]` |

---

### 2.4 Category: `stats` (Statistics & Random)
| Function | Description | Example |
| :--- | :--- | :--- |
| `m.sum(list)` | Sum of numbers | `m.sum([10, 20, 30])` -> `60` |
| `m.avg(list)` / `m.mean(list)` | Arithmetic average | `m.avg([10, 20, 30])` -> `20.0` |
| `m.median(list)` | Median value | `m.median([10, 20, 40])` -> `20` |
| `m.mode(list)` | Most frequent element | `m.mode([1, 2, 2, 3])` -> `2` |
| `m.variance(list)` | Population variance | `m.variance([2, 4, 4, 4, 5, 5, 7, 9])` |
| `m.std(list)` | Standard deviation ($\sigma$) | `m.std([2, 4, 4, 4, 5, 5, 7, 9])` |
| `m.random()` | Random float in `[0.0, 1.0)` | `m.random()` |
| `m.random(max)` | Random integer in `[1, max]` | `m.random(10)` -> `7` |
| `m.random(min, max)` | Random integer in `[min, max]` | `m.random(5, 15)` -> `11` |

---

### 2.5 Category: `trig` (Trigonometry, Constants & Geometry)
| Function / Constant | Description | Example |
| :--- | :--- | :--- |
| `m.pi` | Circle constant $\pi$ | `m.pi` -> `3.141592653589793` |
| `m.e` | Euler's number $e$ | `m.e` -> `2.718281828459045` |
| `m.sin(rad)` | Sine | `m.sin(m.pi / 2)` -> `1.0` |
| `m.cos(rad)` | Cosine | `m.cos(0)` -> `1.0` |
| `m.tan(rad)` | Tangent | `m.tan(m.pi / 4)` -> `1.0` |
| `m.asin(x)`, `m.acos(x)`, `m.atan(x)` | Inverse trigonometric functions | `m.deg(m.asin(1.0))` -> `90.0` |
| `m.deg(rad)` | Converts radians to degrees | `m.deg(m.pi)` -> `180.0` |
| `m.rad(deg)` | Converts degrees to radians | `m.rad(180)` -> `3.14159...` |
| `m.hypot(a, b)` | Hypotenuse $\sqrt{a^2 + b^2}$ | `m.hypot(3, 4)` -> `5` |
| `m.dist(p1, p2)` | 2D / 3D Euclidean distance | `m.dist([0, 0], [3, 4])` -> `5` |
| `m.lerp(a, b, t)` | Linear interpolation $a + t(b - a)$ | `m.lerp(0, 100, 0.5)` -> `50.0` |

---

### 2.6 Category: `special` (Bose Specials)
Unique helper functions tailored for game development, UI layout, finance, and data science:

| Function | Description | Example |
| :--- | :--- | :--- |
| `m.remap(val, in_range, out_range)` | Maps a value from one range to another | `m.remap(50, 0..100, 0..1)` -> `0.5` |
| `m.remap(val, in_min, in_max, out_min, out_max)` | 5-argument alternative for remap | `m.remap(50, 0, 100, 0, 1)` -> `0.5` |
| `m.percent(val, total)` | Calculates what percentage `val` is of `total` | `m.percent(25, 100)` -> `25` |
| `m.percent_of(p, total)` | Calculates $p\%$ of `total` | `m.percent_of(20, 200)` -> `40` |
| `m.percent_change(old, new)` | Calculates percentage increase or decrease | `m.percent_change(100, 150)` -> `50` |

---

## 3. Fearless Architecture & File Integrity

All math implementations strictly conform to BoseLang's engineering standards:
- **Location:** `src/module/math/`
- **File limit:** Every submodule file strictly contains $< 200$ lines (far below the 700-line limit).
- **Core cleanliness:** Zero bloat added to `vm/engine/dispatch.rs` or core opcode handlers.
- **Pure safe Rust:** Zero memory leaks, atomic PRNG generator, zero external dependencies.
