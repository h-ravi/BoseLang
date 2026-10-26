# 13. BoseLang Native JSON Handling

BoseLang me JSON handling ko **"Zero Friction, Zero Resource Leaks, Maximum Developer Joy"** ki philosophy par banaya gaya hai.

Python me `import json` karke `load`, `loads`, `dump`, `dumps` ke beech confuse hona padta hai, aur JavaScript me file handling ke liye `fs` aur JSON parsing ke liye `JSON.parse` ko alag-alag jodna padta hai.

BoseLang me **`json`** ek first-class immutable built-in module hai jo sirf **3 ultra-smart unified commands** ke sath poore duniya ke 100% real-world aur AI workflows ko sambhal leta hai:

1. **`json.read(source)`** — File ya raw AI string ko padhkar native BoseLang `Map` ya `List` banata hai (AI markdown auto-clean ke sath).
2. **`json.write(path, data)`** — BoseLang `Map`, `List` ya raw AI string ko 4-space indented pretty JSON bana kar disk par likhta hai.
3. **`json.valid(source)`** — Bina crash hue check karta hai ki JSON syntax valid hai ya nahi (`true` ya `false`).

---

## 📑 Quick Cheat Sheet

| Command | Arguments | Return Type | Kaam | Memory Footprint |
|---|---|---|---|---|
| **`json.read(source)`** | `source` (file path ya raw text) | `Map` ya `List` | File ya string ko padhkar native BoseLang structure banata hai. Auto-cleans AI markdown. | Object size ke barabar |
| **`json.write(path, data)`** | `path`, `data` (Map, List, ya JSON text) | `Null` | 4 spaces ke indentation ke sath clean pretty JSON file save karta hai. Missing folders auto-create karta hai. | Minimal |
| **`json.valid(source)`** | `source` (file path ya raw text) | `bool` | Check karta hai ki valid JSON maujood hai ya nahi (`true`/`false`). Kabhi crash nahi hota. | Zero allocation |

---

## 1. Data Type Conversion (JSON $\leftrightarrow$ BoseLang)

Jab aap `json.read` call karte hain, to JSON ka har data type seedhe BoseLang ke native type me convert hota hai:

| JSON Type | JSON Example | BoseLang Type | BoseLang Example | `type()` Output |
|---|---|---|---|---|
| **Object** | `{"name": "Bose"}` | **`Map`** | `("name": "Bose")` | `"map"` |
| **Array** | `[10, 20, 30]` | **`List` (1-Based!)** | `[10, 20, 30]` | `"list"` |
| **Integer** | `100` | **`int`** (64-bit) | `100` | `"int"` |
| **Float** | `98.6` | **`point`** (64-bit) | `98.6` | `"point"` |
| **String** | `"Namaste"` | **`text`** (UTF-8) | `"Namaste"` | `"text"` |
| **Boolean** | `true` / `false` | **`bool`** | `true` / `false` | `"bool"` |
| **Null** | `null` | **`Null`** | `Null` | `"Null"` |

> ⚠️ **Golden Rule:** BoseLang me arrays **1-based** hote hain! Agar JSON me `items: ["A", "B", "C"]` hai, to pehla item **`items[1]`** hoga, `items[0]` nahi!

---

## 2. JSON Ko Padhte Kaise Hain? (Two Different Needs)

Real-world coding me JSON padhne ke **do alag-alag maqsad** hote hain:

### A. Programmatic Processing: Data par Logic Lagana (`json.read`)
Jab aapko data me se values nikalni hon, loop chalana ho, ya calculations karni hon:

```bose
/* 1. File read karein -> Yeh Map banayega */
data = json.read("app_settings.json")

/* 2. Values access karein */
out("App Name:", data["app_name"])
out("Theme:", data["theme"])
out("Is Pro:", data["is_pro"])

/* 3. Nested 1-based list access */
out("First Feature (index 1):", data["features"][1])

/* 4. Natural loop */
loop feat from data["features"] {
    out(" - Feature:", feat)
}
```

### B. Visual Pretty-Print: Screen par Sundar Dekhna (`read`)
Aksar developer kehte hain: *"Mujhe code me manipulate nahi karna, bas screen par dekhna hai ki file me kya likha hai."*

Agar aap `out(data)` karenge, to console par ek hi flat line me compact output aayega (jaise Python me `print(dict)`).

Lekin agar aapko screen par **4-space indented formatted view** dekhna hai, to aap direct universal `read()` use kar sakte hain:
```bose
/* File pehle se formatted hai, out(read()) use as-it-is sundar print kar dega: */
out(read("app_settings.json"))
```

Output:
```json
{
    "app_name": "Bose Studio",
    "theme": "Dark",
    "is_pro": true,
    "features": [
        "Live Highlighting",
        "Fast Bytecode VM",
        "Native AI Integration"
    ]
}
```

---

## 3. In-Memory Data ko Modify Kaise Karein?

Kyunki `json.read` se mila hua data **native BoseLang Map aur List** hota hai, isliye aapko kisi naye JSON command ki zaroorat nahi hoti. Saare regular collection operations seedhe kaam karte hain:

```bose
config = json.read("config.json")

/* 1. Field update karna */
config["theme"] = "Cyberpunk"

/* 2. Naya field add karna */
config["last_login"] = 1718000000

/* 3. Field remove karna */
config.remove("temp_token")

/* 4. List me naya item add karna */
config["features"].add("Auto Sync")

/* 5. Keys aur values inspect karna */
out("All config keys:", config.keys())

/* 6. Modify karke wapas save kar do! */
json.write("config.json", config)
out("Config updated successfully!")
```

---

## 4. Memory-Safe Big Data & AI Streaming (`.jsonl` / NDJSON)

Machine Learning datasets, cloud server logs, aur AI training files aksar **100 MB se 10 GB** ki hoti hain. Inme har line par ek alag JSON object hota hai (jise **JSON Lines** ya **NDJSON** kehte hain).

Agar aap 5 GB ki file ko poora RAM me padhenge, to computer memory full hokar crash ho jayega (OOM).

BoseLang me ise **`read_stream`** aur **`json.read`** ke sath sirf **constant ~8 KB RAM** me chala sakte hain:

```bose
/* 10 GB file ko 8 KB RAM me process karein! */
high_score_count = 0

loop line from read_stream("massive_ai_dataset.jsonl") {
    /* Line-by-line JSON parse */
    record = json.read(line)

    when record["score"] >= 95 {
        high_score_count += 1
        out("Candidate:", record["username"], "Score:", record["score"])
    }
}

out("Total Top Performers:", high_score_count)
```

**Stream Ke Fayde:**
* Ek waqt me sirf 1 line memory me hoti hai.
* Trailing `\r\n` automatically trim ho jate hain.
* Agar file me header line ho to open range `2..` use kar sakte hain: `read_stream("data.jsonl", 2..)`.

---

## 5. AI / LLM Integration & "Auto-Safai" (Automatic Cleanup)

AI models (jaise Groq, OpenAI, Gemini) se aane wale JSON ke sath do sabse badi dikkat aati hai:
1. **Markdown Code Blocks:** AI text ko ` ```json ... ``` ` me wrap kar deta hai.
2. **Conversational Chit-Chat:** AI aage-peeche baatein likh deta hai:
   `"Sure! Here is the JSON configuration you asked for:\n```json\n{\"id\": 101}\n```\nHope this helps!"`

Traditional languages me iske liye regular expressions (regex) ya string slicing likhni padti hai.

BoseLang me **Auto-Safai Engine built-in** hai:

### A. Auto-Clean Write:
```bose
ai_reply = "Sure! Here is the JSON:\n```json\n{\"model\":\"Qwen-3.8-27B\",\"status\":\"ready\"}\n```\nEnjoy!"

/* BoseLang chit-chat aur markdown backticks ko auto-strip karke clean JSON likh dega: */
json.write("ai_config.json", ai_reply)
```

### B. Direct RAM String to Map:
```bose
/* Bina file likhe, messy string se seedhe Map banayein: */
ai_map = json.read(ai_reply)
out("Model Name:", ai_map["model"])
out("Status:", ai_map["status"])
```

---

## 6. Crash-Proof Validation (`json.valid`)

Agar AI ne toota hua ya adhoora JSON diya (jaise bracket miss ho gaya), to bina crash hue code ko protect karne ke liye **`json.valid(source)`** ka use karein:

```bose
ai_raw = net.post("https://api.groq.com/...", payload, headers)

/* Check validity without any panic or crash */
when json.valid(ai_raw) {
    clean_data = json.read(ai_raw)
    json.write("results.json", clean_data)
    out("Valid AI response processed successfully!")
} otherwise {
    out("Warning: AI returned corrupted or broken JSON!")
}
```

> `json.valid()` file path par bhi chalta hai: `when json.valid("settings.json") { ... }`.

---

## 7. Fail-Fast Error Diagnostics

Agar JSON file ya string me koi syntax mistake hoti hai, to BoseLang exact **line number, column number aur helpful hint** ke sath error deta hai:

### A. Missing File Error:
```text
File Error: File 'missing.json' not found.
  Hint: Check if the file exists using 'exist("missing.json")' before calling json.read().
```

### B. Malformed / Broken Syntax Error:
Agar JSON file me trailing comma ya missing closing bracket hai:
```text
JSON Error: Malformed JSON syntax (line 4, col 12): expected `,` or `}`.
  Hint: Verify quotes around keys, remove trailing commas, and ensure brackets match.
```

### C. Insufficient Arguments Error:
```bose
json.read()
/* Error: Argument Error: json.read() requires a file path argument. */
/*   Example: json.read("data.json") */

json.write("out.json")
/* Error: Argument Error: json.write() requires 2 arguments: path and data. */
/*   Example: json.write("data.json", my_map) */
```

---

## 8. Concise Aliasing (`fix j = json`)

BoseLang ke modules first-class objects hote hain, isliye aap unhe chhota alias de sakte hain:

```bose
fix j = json

data = j.read("data.json")
when j.valid(data) {
    j.write("backup.json", data)
}
```

---

## 9. Complete End-to-End Real-World Example

```bose
/* Complete Real-World Script: AI Data Processor */

block auto main() {
    out("==========================================")
    out("🚀 BoseLang Real-World JSON Workflow")
    out("==========================================")

    /* Step 1: Simulate Messy AI API Response */
    ai_raw = "Hello! Here is the telemetry report:\n```json\n{\n    \"service\": \"Auth-Worker\",\n    \"healthy\": true,\n    \"latency_ms\": 4.2,\n    \"active_endpoints\": [\"/login\", \"/token\", \"/refresh\"]\n}\n```\nAll systems operational!"

    /* Step 2: Validate without crashing */
    when json.valid(ai_raw) {
        out("[1] AI Response is valid JSON!")

        /* Step 3: Parse directly to in-memory Map */
        telemetry = json.read(ai_raw)
        out("[2] Service Name:", telemetry["service"])
        out("[3] Latency:", telemetry["latency_ms"], "ms")
        out("[4] Primary Endpoint (1-based index):", telemetry["active_endpoints"][1])

        /* Step 4: Modify fields */
        telemetry["active_endpoints"].add("/logout")
        telemetry["last_check"] = 1718005000

        /* Step 5: Auto-create directory and save 4-space formatted JSON */
        output_file = "logs/telemetry_clean.json"
        json.write(output_file, telemetry)
        out("[5] Saved formatted report to:", output_file)

        /* Step 6: View formatted file on screen */
        out("\n--- Pretty File Content ---")
        out(read(output_file))
    } otherwise {
        out("❌ Fatal: Failed to extract valid JSON from response.")
    }
}
```
