# 11. BoseLang Universal File Handling

BoseLang me file handling ko **"Zero Boilerplate, Zero Resource Leaks, Maximum Speed"** ki philosophy par design kiya gaya hai.

Python ya C ki tarah yahan `open()` karne ya manual `close()` karne ka koi jhanjhat nahi hota. File kholna, memory-safe tareeqe se data padhna ya likhna, aur file lock ko instantly OS me band karna — yeh sab BoseLang internally auto-handle karta hai.

---

## 📑 Core Functions Cheat Sheet

| Function | Limit / Range | Return Type | Kaam | RAM Usage |
|---|---|---|---|---|
| **`read(path, limit?)`** | `read("f.txt", 100)` ya `1..50` ya `10..` | `Text` | Poori file ya characters slice karke string return karta hai. | File size ke barabar |
| **`read_list(path, limit?)`** | `read_list("f.txt", 10)` ya `2..10` ya `2..` | `List` | File ki lines ko `List` of strings bana kar deta hai. Fast newline scanner. | Lines ke barabar |
| **`read_stream(path, limit?)`** | `read_stream("f.csv", 2..)` | `Stream` | **Lazy Stream**: 8 KB buffer me disk se 1-1 line loop ko stream karta hai. | **Constant ~8 KB** |
| **`write(path, data)`** | Text ya List | `Null` | Nayi file banata hai ya purani overwrite karta hai (List aane par auto `\n`). | Minimal |
| **`append(path, data)`** | Text ya List | `Null` | Aakhir me text ya list jodta hai (File na ho to auto-create). | Minimal |
| **`create(path)`** | None | `bool` | Khali file create karta hai agar pehle se na ho. | 0 |
| **`exist(path)`** | None | `bool` | Check karta hai hard disk par file maujood hai ya nahi (`true`/`false`). | 0 |
| **`delete(path)`** | None | `bool` | File ko safely hard drive se delete karta hai. | 0 |

> **Note:** Yeh saare functions direct standalone bhi chalte hain (jaise `read(...)`) aur **`file.`** universal namespace me bhi chalte hain (jaise `file.read(...)`).

---

## 1. File Text Read Karna (`read`)

Chhoti ya medium files (config, JSON, templates) ko poori string ke roop me read karne ke liye:

### A. Poori File:
```bose
content = read("notes.txt")
out(content)
```

### B. Shuru ke Characters (`read(path, count)`):
```bose
first_hundred = read("article.txt", 100)
out(first_hundred)  /* Shuru ke 100 UTF-8 characters */
```

### C. Character Range (`read(path, start..end)` ya `start..`):
```bose
slice = read("book.txt", 1..50)    /* Chars 1 se 50 tak */
rest  = read("book.txt", 51..)     /* Char 51 se aakhri char tak */
```

---

## 2. File Lines ko List me Lena (`read_list`)

Jab aapko file ki lines ko list ke roop me chahiye taaki aap `lines[1]` ya `len(lines)` kar sakein:

### A. Saari Lines:
```bose
lines = read_list("servers.txt")
out("Total servers:", len(lines))
out("Primary server:", lines[1])   /* 1-based index */
```

### B. Shuru ki N Lines:
```bose
top5 = read_list("scores.txt", 5)  /* Shuru ki 5 lines */
```

### C. Specific Line Range & Fast-Forward (`read_list(path, 300000..350000)`):
Agar file me 5 lakh lines hain aur aapko 3 lakh se 3.5 lakh tak ki lines chahiye:
```bose
batch = read_list("big_data.csv", 300000..350000)
```
- **Zero Memory Skip:** Pehli 2,99,999 newlines (`\n`) ko CPU SIMD byte buffer se 0.02 second me skip karega bina kisi String allocation ke.
- 3,00,000 se 3,50,000 tak ki 50,000 lines ki List banayega.
- 3,50,000 par turant stop ho kar file handle close kar dega.

### D. Header Skip karke Aakhri tak (`2..`):
```bose
data_rows = read_list("data.csv", 2..)  /* Line 2 se end tak */
```

---

## 3. Badi Files ke liye Lazy Streaming (`read_stream`)

Jab file **10 MB se 100 GB** ki ho (Big CSV, server logs, million URLs), tab file ko List me lena memory crash (OOM) kar deta hai. Wahan **`read_stream`** ka use karein.

### A. Pure Stream Loop:
```bose
/* Poori file RAM me nahi aayegi, 1-1 line stream hogi! */
loop line from read_stream("huge_server.log") {
    when line.find("ERROR") {
        out("Found alert:", line)
    }
}
```
* **Memory footprint:** Hamesha **constant ~8 KB**.
* Trailing `\r\n` (Windows) aur `\n` (Linux) automatically clean ho jate hain.

### B. CSV Header Skip karna (`2..` Open Range):
```bose
loop row from read_stream("users.csv", 2..) {
    /* Line 1 (Header) skip ho gaya! Direct data row mili */
    out("Processing user:", row)
}
```

### C. Target tak stream karna:
```bose
loop row from read_stream("dataset.csv", 100) {
    /* Sirf pehli 100 lines stream hongi, 100 ke baad file auto-close */
    out(row)
}
```

### D. Re-Iterate Stream (Do baar loop chalana):
BoseLang streams are auto-rewindable! Ek hi stream variable par agar aap dubara loop chalate hain:
```bose
s = read_stream("data.csv")

loop line from s {
    out("Pass 1:", line)
}

/* Doosra loop — automatically disk se rewind ho kar stream hoga */
loop line from s {
    out("Pass 2:", line)
}
```

---

## 4. Smart File Writing (`write`)

`write` se nayi file create hoti hai ya purani overwrite hoti hai. Yeh **String aur List dono ko natively support karta hai**:

### A. String Likhna:
```bose
write("message.txt", "Give me blood, and I will give you freedom!\n")
```

### B. List Likhna (Auto-Newline):
Agar aap List pass karte hain, toh BoseLang har item ke baad automatically `\n` lagata hai:
```bose
names = ["Amit", "Rohit", "Rahul"]
write("students.txt", names)
/* File me banega:
   Amit
   Rohit
   Rahul
*/
```

---

## 5. Smart File Appending (`append`)

`append` purani file ke aakhir me naya data jodta hai. Agar file pehle se maujood nahi hai, toh yeh **automatically nayi file create** kar deta hai.

```bose
/* String append */
append("app.log", "Task started at 10:00 AM\n")

/* List append (har item new line par judega) */
new_users = ["Pooja", "Vikas"]
append("users.txt", new_users)
```

---

## 6. Utilities: `create`, `exist`, `delete`

### Khali File Banana (`create`):
```bose
created = create("process.lock")
when created {
    out("Marker file created successfully.")
}
```

### File Check Karna (`exist`):
```bose
when exist("database.sqlite") {
    out("Database ready.")
} otherwise {
    out("Database missing! Creating initial setup...")
}
```

### File Delete Karna (`delete`):
```bose
deleted = delete("temp_cache.tmp")
when deleted {
    out("Cache removed.")
}
```

---

## 7. Universal `file` Module Namespace

Saare file functions ko aap `file.` namespace ke sath bhi call kar sakte hain:

```bose
when file.exist("config.env") {
    content = file.read("config.env")
    lines = file.read_list("config.env")
    file.append("audit.log", "Config read by user\n")
}
```

---

## 8. Educational Error Guards & Safety

BoseLang me galat file handling par cryptic crash nahi aata, balki helpful Hints milte hain:

### A. Reversed Range Error (`10..2`):
```text
Range Error: Invalid line range 10..2 (start line 10 is greater than end line 2).
  Hint: In BoseLang, ranges must go forward like '2..10' or use an open range like '2..'.
```

### B. Negative ya Zero Index Error (`0..10` ya `-5`):
```text
Range Error: Line numbers must be positive (found 0).
  Hint: BoseLang indexing is 1-based (first line is line 1). Use '1..10' or '2..'.
```

### C. Stream Index / Len Error:
```text
Stream Error: Streams cannot be indexed with '[ ]' because data is read dynamically from disk.
  Hint: Iterate with 'loop line from stream { ... }' or use 'read_list()' if you need indexed access like 'lines[1]'.
```

### D. File Excel me khuli ho (Permission Denied):
```text
File Error: Cannot access 'data.csv': Permission denied.
  Hint: The file may be locked or open in another program (like Microsoft Excel). Close it and retry.
```

### E. OS Protection Shield:
Agar koi galti se ya script me operating system ki critical files (`C:\Windows`, `System32`, `/etc`, `/bin`) ko overwrite ya delete karne ki koshish kare:
```text
Security Error: Deletion blocked on protected system path 'C:\Windows\...'.
  Hint: BoseLang prevents accidental deletion of operating system files.
```

---

## 🚀 Complete Real-World Script: 50,000 URLs Downloader

```bose
url_file = "urls.txt"

when exist(url_file) == false {
    /* Test URLs prepare karo */
    sample = [
        "https://example.com/api/item1",
        "https://example.com/api/item2",
        "https://example.com/api/item3"
    ]
    write(url_file, sample)
    out("Created sample URL file.")
}

out("=== Processing URLs via Lazy Stream ===")

/* Memory-safe streaming: 1-1 line disk se aayegi */
loop url from read_stream(url_file) {
    when url == "" {
        skip    /* Blank line ignore karo */
    }
    out("Fetching: " + url)
    /* result = net.get(url) */
}

out("All URLs processed successfully with zero RAM spikes!")
```
