# 15. Level 7 Time Module Master Guide (`time`, `DateTime` & Capability Security)

Status: **Certified Level 7 Architecture**  
Standard: **Human-First, 1-Based Indexing, Zero External Dependencies, Pure Safe Rust**

---

## 🌟 Introduction: The BoseLang Time Philosophy

In traditional programming languages, handling dates and time has historically been one of the biggest sources of bugs and developer frustration:
- **JavaScript** uses an unnatural 0-based month system (`0 = January`, `11 = December`), confusing every beginner, and requires heavy third-party npm packages like `moment.js` or `date-fns` for basic formatting.
- **Python** scatters its time utilities across four disconnected libraries (`time`, `datetime`, `calendar`, `zoneinfo`) and uses cryptic C-style format strings (`%Y-%m-%d %H:%M:%S`).
- **Java / C++** historically suffered from confusing timestamp arithmetic and mutability bugs.

**BoseLang solves this once and for all:**
1. **1-Based Counting Throughout:** Months are `1` to `12`, days are `1` to `31`, and weekdays are `1` to `7` (Monday = 1, Sunday = 7).
2. **One Unified Module:** Everything you need—current clocks, calendar breakdowns, formatting, date math, precision stopwatches, and relative time—lives inside **one single `time` module**.
3. **Readable Formats:** Say goodbye to `%d %m %Y`. Use clean tokens like `DD-MM-YYYY` and `hh:mm A`.
4. **Built for Real Applications:** Direct support for 24-hour and 12-hour time, social media relative time (`ago()`, `until()`), and native Indian localization (`indian_fy()`, Hindi calendar names).
5. **Capability-Based Security:** Protect your systems by granting only the exact time capabilities a function or script needs.

---

## 📚 Complete Chapter Index

1. [Accessing Time & Capability Security](#1-accessing-time--capability-security)
2. [Instant Clocks & Epoch Timestamps](#2-instant-clocks--epoch-timestamps)
3. [The `DateTime` Object: Properties Deep-Dive](#3-the-datetime-object-properties-deep-dive)
4. [Formatting Engine: Custom Dates & Times](#4-formatting-engine-custom-dates--times)
5. [Date Arithmetic & Safe Calendar Math](#5-date-arithmetic--safe-calendar-math)
6. [Calendar Queries & Leap Year Logic](#6-calendar-queries--leap-year-logic)
7. [Stopwatch Timer & Execution Pauses](#7-stopwatch-timer--execution-pauses)
8. [Bose Specials: Indian FY, Hindi & Relative Time](#8-bose-specials-indian-fy-hindi--relative-time)
9. [Complete Method & Property Reference Table](#9-complete-method--property-reference-table)

---

## 1. Accessing Time & Capability Security

In BoseLang, `time` is a core protected module. You can access it directly or assign it to an immutable variable with `fix`.

### 1.1 Full Unrestricted Access
```bose
fix t = time

out(t.today())              // "24-10-2026"
out(t.now().text())         // "24 October 2026, 12:50 PM"
```

### 1.2 Capability Sandboxing & Power Transfer
When writing modular code, running third-party plugins, or building secure backend tasks, you can restrict what parts of the `time` module a script or function can execute.

BoseLang organizes all time features into **6 Official Categories**:

| Category | Included Methods & Powers | Ideal Use Case |
| :--- | :--- | :--- |
| **`clock`** | `now`, `today`, `time24`, `time12`, `utc_now`, `stamp`, `stamp_ms`, `from_stamp` | Read-only current timestamp access. |
| **`calendar`** | `year`, `month`, `month_name`, `day`, `weekday`, `weekday_name`, `is_leap`, `days_in_month`, `days_in_year`, `is_weekend`, `year_day` | Date logic & calendar queries. |
| **`format`** | `format`, `iso`, `text` | Display & string conversions. |
| **`calc`** | `add_days`, `sub_days`, `add_hours`, `sub_hours`, `add_mins`, `add_months`, `diff` | Date shifting and scheduling math. |
| **`timer`** | `timer`, `start_timer`, `stop_timer`, `stop`, `elapsed`, `sleep`, `sleep_ms`, `clock` | Profiling, stopwatches, and pauses. |
| **`special`** | `ago`, `until`, `indian_fy`, `fy_quarter`, `weekday_name_hi`, `month_name_hi` | Indian financial year, Hindi & relative time. |

#### Example: Granting Specific Categories
```bose
/* Sandbox: Allow calendar and formatting only. Sleep and timer are blocked! */
fix t_safe = time(clock, calendar, format)

out(t_safe.today())         // Allowed! ➔ "24-10-2026"
out(t_safe.is_leap(2024))   // Allowed! ➔ true

/* If an untrusted script attempts to sleep or use timer: */
// t_safe.sleep(5)
// Error: Security Error: Capability 'sleep' is not granted to this time object.
//   Hint: Grant capability when initializing: 'time(timer)' or 'time(sleep)'.
```

#### Example: Granular Function Powers
You can even grant individual function names:
```bose
fix t_min = time(today, is_leap)
out(t_min.today())          // Allowed!
out(t_min.is_leap(2026))    // Allowed!
// t_min.now()              // Blocked!
```

---

## 2. Instant Clocks & Epoch Timestamps

Timestamps are essential for saving records in databases, comparing events, and sending HTTP API payloads.

```bose
fix t = time

/* 1. t.stamp() -> Unix Epoch in Seconds (since Jan 1, 1970) */
sec = t.stamp()
out("Seconds timestamp:", sec)
// Output: Seconds timestamp: 1792824062

/* 2. t.stamp_ms() -> Unix Epoch in Milliseconds */
ms = t.stamp_ms()
out("Milliseconds timestamp:", ms)
// Output: Milliseconds timestamp: 1792824062000

/* 3. t.today() -> Direct Date String (DD-MM-YYYY) */
out("Today:", t.today())
// Output: Today: 24-10-2026

/* 4. t.time24 -> Current 24-Hour Time String (HH:mm:ss) */
out("24-Hour Time:", t.time24)
// Output: 24-Hour Time: 14:30:15

/* 5. t.time12 -> Current 12-Hour Time String (hh:mm:ss AM/PM) */
out("12-Hour Time:", t.time12)
// Output: 12-Hour Time: 02:30:15 PM

/* 6. t.from_stamp(secs) -> Reconstruct DateTime object from epoch integer */
historical = t.from_stamp(1600000000)
out("Historical date:", historical.format("DD-MM-YYYY"))
// Output: Historical date: 13-09-2020
```

---

## 3. The `DateTime` Object: Properties Deep-Dive

Calling `now = t.now()` or `utc = t.utc_now()` produces a rich, queryable `DateTime` object. Every property can be accessed directly using standard dot syntax (`now.property`).

```bose
fix t = time
now = t.now()
```

### 3.1 Date Breakdown
| Property | Type | Description | Example Output |
| :--- | :---: | :--- | :--- |
| `now.year` | `int` | Full 4-digit calendar year | `2026` |
| `now.month` | `int` | 1-based month number (1 to 12) | `10` |
| `now.month_name` | `text` | Full English month name | `"October"` |
| `now.day` | `int` | Day of the month (1 to 31) | `24` |
| `now.weekday` | `int` | 1-based weekday (1 = Monday, 7 = Sunday) | `6` |
| `now.weekday_name` | `text` | Full English weekday name | `"Saturday"` |
| `now.year_day` | `int` | Day of the year (1 to 366) | `297` |
| `now.is_weekend` | `bool` | `true` if Saturday or Sunday | `true` |

### 3.2 Time Breakdown
| Property | Type | Description | Example Output |
| :--- | :---: | :--- | :--- |
| `now.hour` | `int` | Hour in 24-hour format (0 to 23) | `14` |
| `now.hour12` | `int` | Hour in 12-hour format (1 to 12) | `2` |
| `now.minute` | `int` | Minute (0 to 59) | `30` |
| `now.second` | `int` | Second (0 to 59) | `15` |
| `now.ampm` | `text` | Upper-case meridiem (`"AM"` or `"PM"`) | `"PM"` |
| `now.time24` | `text` | 24-hour time formatted as `HH:mm:ss` | `"14:30:15"` |
| `now.time12` | `text` | 12-hour time formatted as `hh:mm:ss A` | `"02:30:15 PM"` |
| `now.offset` | `text` | Local timezone UTC offset | `"+05:30"` |

### 3.3 Practical Example: Working with Properties
```bose
fix t = time
now = t.now()

when now.is_weekend {
    out("It's {now.weekday_name}! Time to relax or code BoseLang! 🎉")
} otherwise {
    out("Work day: {now.weekday_name}. Focus and build! 💼")
}

out("Current Time: {now.time12} (Zone: {now.offset})")
```

---

## 4. Formatting Engine: Custom Dates & Times

BoseLang replaces confusing format codes with clear, readable tokens.

### 4.1 Token Reference Table

| Token | Meaning | Example for Oct 24, 2026, 14:05:09 |
| :---: | :--- | :--- |
| `YYYY` | 4-digit year | `2026` |
| `YY` | 2-digit year | `26` |
| `MM` | 2-digit month with leading zero | `10` |
| `M` | 1 or 2-digit month | `10` (or `3` for March) |
| `DD` | 2-digit day of month with leading zero | `24` |
| `D` | 1 or 2-digit day of month | `24` (or `5` for 5th) |
| `HH` | 24-hour format (`00` to `23`) | `14` |
| `hh` | 12-hour format (`01` to `12`) | `02` |
| `mm` | 2-digit minute (`00` to `59`) | `05` |
| `ss` | 2-digit second (`00` to `59`) | `09` |
| `A` | Uppercase AM/PM | `PM` |
| `a` | Lowercase am/pm | `pm` |

### 4.2 Formatting Examples

```bose
fix t = time
now = t.now()

/* 1. Indian Standard Format (DD-MM-YYYY) */
out(now.format("DD-MM-YYYY"))
// Output: 24-10-2026

/* 2. Slash format with 12-hour time */
out(now.format("DD/MM/YYYY hh:mm A"))
// Output: 24/10/2026 02:05 PM

/* 3. Railway / 24-hour format */
out(now.format("YYYY-MM-DD HH:mm:ss"))
// Output: 2026-10-24 14:05:09

/* 4. Global ISO 8601 Standard */
out(now.iso())
// Output: 2026-10-24T14:05:09+05:30

/* 5. Natural Human Text */
out(now.text())
// Output: 24 October 2026, 02:05 PM
```

---

## 5. Date Arithmetic & Safe Calendar Math

BoseLang makes time math intuitive and crash-free. You don't have to manually calculate seconds or worry about day-count boundaries.

```bose
fix t = time
now = t.now()

/* 1. Add Days */
tomorrow = now.add_days(1)
out("Tomorrow:", tomorrow.format("DD-MM-YYYY"))
// Output: Tomorrow: 25-10-2026

/* 2. Subtract Days */
two_days_ago = now.sub_days(2)
out("2 Days Ago:", two_days_ago.format("DD-MM-YYYY"))
// Output: 2 Days Ago: 22-10-2026

/* 3. Add / Subtract Hours */
later = now.add_hours(5)
out("5 Hours Later:", later.format("hh:mm A"))
// Output: 5 Hours Later: 07:05 PM

earlier = now.sub_hours(3)
out("3 Hours Earlier:", earlier.format("hh:mm A"))
// Output: 3 Hours Earlier: 11:05 AM

/* 4. Add Minutes */
meeting = now.add_mins(45)
out("Meeting Time:", meeting.format("hh:mm A"))

/* 5. Safe Month Math (Clamped to Month End) */
/* Jan 31 + 1 month automatically clamps to Feb 28 (or Feb 29 in leap year) */
next_month = now.add_months(1)
out("Next Month:", next_month.format("DD-MM-YYYY"))
// Output: Next Month: 24-11-2026

/* 6. Difference between Two Dates (diff) */
d1 = t.now()
d2 = d1.add_days(10)
difference = d1.diff(d2)

out("Days difference:", difference.days)       // 10
out("Hours difference:", difference.hours)     // 240
out("Seconds difference:", difference.seconds) // 864000
```

---

## 6. Calendar Queries & Leap Year Logic

Direct functions to query calendar constraints without writing custom formula loops:

```bose
fix t = time

/* 1. Leap Year Check (is_leap) */
out("Is 2024 leap year?", t.is_leap(2024))   // true
out("Is 2026 leap year?", t.is_leap(2026))   // false
out("Is 2000 leap year?", t.is_leap(2000))   // true (century divisible by 400)
out("Is 1900 leap year?", t.is_leap(1900))   // false (century divisible by 100 but not 400)

/* 2. Days in Month (days_in_month) */
out("Days in Feb 2024 (Leap):", t.days_in_month(2024, 2))  // 29
out("Days in Feb 2026:", t.days_in_month(2026, 2))         // 28
out("Days in July:", t.days_in_month(2026, 7))             // 31
out("Days in April:", t.days_in_month(2026, 4))            // 30

/* 3. Days in Year (days_in_year) */
out("Total days in 2026:", t.days_in_year(2026))           // 365
out("Total days in 2024:", t.days_in_year(2024))           // 366
```

---

## 7. Stopwatch Timer & Execution Pauses

Measuring the exact speed of your algorithms and loops should be effortless. BoseLang provides an intuitive stopwatch model: **Start** and **Stop**.

```bose
fix t = time

/* 1. Start the Stopwatch */
sw = t.timer()
// (You can also write: sw = t.start_timer())

/* Run your computation, loop, or file download */
total = 0
loop i from 1..100000 {
    total += i
}

/* 2. Stop the Stopwatch: Computes and freezes the duration */
time_taken = sw.stop_timer()
// (You can also write: time_taken = sw.stop())

out("Result:", total)
out("Execution time:", time_taken, "seconds")
// Output: Execution time: 0.003412 seconds

/* 3. Mid-run Check (elapsed) */
/* If you want to check the stopwatch without stopping it: */
sw2 = t.timer()
// ... halfway work ...
out("Lap 1:", sw2.elapsed())
// ... finish work ...
out("Final:", sw2.stop())

/* 4. Pausing Execution (sleep) */
t.sleep(1)        // Pauses execution for 1 second
t.sleep(0.5)      // Pauses execution for half a second
t.sleep_ms(250)   // Pauses execution for 250 milliseconds
```

---

## 8. Bose Specials: Indian FY, Hindi & Relative Time

BoseLang is uniquely crafted with first-class support for real human applications and Indian business standards.

### 8.1 Relative Time (`ago` and `until`)
Building social media feeds, comment timestamps, or meeting reminders usually requires heavy external packages. In BoseLang, it's native:

```bose
fix t = time
now = t.now()

/* 1. 'ago()' for past timestamps */
comment_time = now.sub_mins(5)
out("Comment posted:", comment_time.ago())
// Output: Comment posted: 5 minutes ago

yesterday_post = now.sub_days(1)
out("Post created:", yesterday_post.ago())
// Output: Post created: 1 day ago

/* 2. 'until()' for future events */
event_time = now.add_hours(3)
out("Webinar starts:", event_time.until())
// Output: Webinar starts: in 3 hours

flight_time = now.add_days(4)
out("Flight departure:", flight_time.until())
// Output: Flight departure: in 4 days
```

### 8.2 Indian Financial Year (`indian_fy` & `fy_quarter`)
In India, the financial, accounting, GST, and tax year runs from **April 1 to March 31**. Traditional languages force developers to write custom conditional functions for this. BoseLang makes it built-in:

```bose
fix t = time
now = t.now()

/* Current Financial Year */
out("Financial Year:", now.indian_fy())
// For October 2026: Output: Financial Year: 2026-27

/* Current Financial Quarter */
/* Q1: Apr-Jun, Q2: Jul-Sep, Q3: Oct-Dec, Q4: Jan-Mar */
out("FY Quarter:", now.fy_quarter())
// For October: Output: FY Quarter: 3
```

### 8.3 Shuddh Hindi Localization
Dedicated to the heritage of Netaji Subhash Chandra Bose, BoseLang supports native Hindi calendar names:

```bose
fix t = time
now = t.now()

out("Aaj ka din:", now.weekday_name_hi)
// Output: Aaj ka din: शनिवार

out("Kaun sa mahina hai:", now.month_name_hi)
// Output: Kaun sa mahina hai: अक्टूबर
```

---

## 9. Complete Method & Property Reference Table

| Target | Method / Property | Description | Return Type |
| :--- | :--- | :--- | :---: |
| `time` | `t.now()` | Current local `DateTime` object | `DateTime` |
| `time` | `t.utc_now()` | Current UTC `DateTime` object | `DateTime` |
| `time` | `t.today()` | Today's date string (`DD-MM-YYYY`) | `text` |
| `time` | `t.time24` | Current time in 24-hour format | `text` |
| `time` | `t.time12` | Current time in 12-hour format | `text` |
| `time` | `t.stamp()` | Unix epoch timestamp (seconds) | `int` |
| `time` | `t.stamp_ms()` | Unix epoch timestamp (milliseconds) | `int` |
| `time` | `t.from_stamp(n)` | Reconstructs `DateTime` from timestamp | `DateTime` |
| `time` | `t.is_leap(year)` | Checks if year is a leap year | `bool` |
| `time` | `t.days_in_month(y, m)` | Number of days in specified month | `int` |
| `time` | `t.days_in_year(year)` | Total days in year (365 or 366) | `int` |
| `time` | `t.timer()` | Starts a precision monotonic stopwatch | `Timer` |
| `time` | `t.sleep(sec)` | Pauses execution for $n$ seconds | `Null` |
| `time` | `t.sleep_ms(ms)` | Pauses execution for $n$ milliseconds | `Null` |
| `time` | `t.clock()` | Raw high-resolution monotonic seconds | `point` |
| `DateTime` | `.year` | 4-digit calendar year | `int` |
| `DateTime` | `.month` | 1-based month number (1 to 12) | `int` |
| `DateTime` | `.month_name` | Full English month name | `text` |
| `DateTime` | `.day` | Day of the month (1 to 31) | `int` |
| `DateTime` | `.weekday` | 1-based day of week (Mon=1, Sun=7) | `int` |
| `DateTime` | `.weekday_name` | Full English day name | `text` |
| `DateTime` | `.hour` | Hour in 24-hour format (0 to 23) | `int` |
| `DateTime` | `.hour12` | Hour in 12-hour format (1 to 12) | `int` |
| `DateTime` | `.minute` | Minute (0 to 59) | `int` |
| `DateTime` | `.second` | Second (0 to 59) | `int` |
| `DateTime` | `.ampm` | `"AM"` or `"PM"` string | `text` |
| `DateTime` | `.time24` | 24-hour formatted string | `text` |
| `DateTime` | `.time12` | 12-hour formatted string | `text` |
| `DateTime` | `.offset` | Timezone UTC offset (`"+05:30"`) | `text` |
| `DateTime` | `.year_day` | Day of year (1 to 366) | `int` |
| `DateTime` | `.is_weekend` | `true` if Saturday or Sunday | `bool` |
| `DateTime` | `.format(pat)` | Custom formatted date-time string | `text` |
| `DateTime` | `.iso()` | Standard ISO 8601 formatted string | `text` |
| `DateTime` | `.text()` | Natural human-readable date-time | `text` |
| `DateTime` | `.add_days(n)` | Shifts date forward by $n$ days | `DateTime` |
| `DateTime` | `.sub_days(n)` | Shifts date backward by $n$ days | `DateTime` |
| `DateTime` | `.add_hours(n)` | Shifts time forward by $n$ hours | `DateTime` |
| `DateTime` | `.sub_hours(n)` | Shifts time backward by $n$ hours | `DateTime` |
| `DateTime` | `.add_mins(n)` | Shifts time forward by $n$ minutes | `DateTime` |
| `DateTime` | `.add_months(n)` | Shifts date forward by $n$ months | `DateTime` |
| `DateTime` | `.diff(other)` | Difference map (`days`, `hours`, etc.)| `map` |
| `DateTime` | `.ago()` | Relative past time string | `text` |
| `DateTime` | `.until()` | Relative future time string | `text` |
| `DateTime` | `.indian_fy()` | Indian Financial Year string | `text` |
| `DateTime` | `.fy_quarter()` | Indian Financial Quarter (1 to 4) | `int` |
| `DateTime` | `.weekday_name_hi` | Shuddh Hindi day name | `text` |
| `DateTime` | `.month_name_hi` | Shuddh Hindi month name | `text` |
| `Timer` | `.stop_timer()` / `.stop()` | Freezes stopwatch & returns elapsed seconds | `point` |
| `Timer` | `.elapsed()` | Checks running elapsed seconds without stopping | `point` |
