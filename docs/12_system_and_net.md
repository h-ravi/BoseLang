# 12. System & Net Engine Guide (`system`, `net`, `fix cmd = system`)

Status: **Certified Level 5 Architecture**

BoseLang provides two dedicated, fearlessly protected built-in engines for Operating System and Internet communication:
1. **`system` Engine**: Process execution, CLI arguments, environment variables, and thread sleep.
2. **`net` Engine**: Native HTTP GET, POST requests, custom headers, and REST/AI API communication.

---

## 1. System Engine (`system`)

In BoseLang, `system` is an immutable, core system object.

### 1.1 Aliasing with `fix cmd = system`
If you prefer a shorter name, you can alias `system` using `fix`:
```bose
fix cmd = system

/* Now cmd has all the powers of system */
res = cmd.run("echo BoseLang is Fearless!")
out(res.trim())
```

### 1.2 System Methods & Global Built-ins
All system capabilities work either via `system.<method>()`, via an alias like `cmd.<method>()`, or directly as global functions:

| Method | Global Built-in | Description | Return Type |
| :--- | :--- | :--- | :--- |
| `system.run(cmd)` | `run(cmd)` | Executes terminal/OS command and captures stdout | `text` |
| `system.args()` | `args()` | Returns command-line arguments passed to script | `list` of `text` |
| `system.env(key)` | `env(key)` | Reads environment variable from OS or automatically from local `.env` file | `text` or `Null` |
| `system.sleep(secs)` | `sleep(secs)` | Pauses execution for given seconds (e.g. `0.5`, `2`) | `Null` |

### 1.3 Examples
```bose
fix cmd = system

/* 1. Terminal Process Execution */
dir_output = cmd.run("dir")

/* 2. Reading Environment Variables (OS or .env file) */
os_name = cmd.env("OS")                  /* from Windows OS */
api_key = env("GROQ_API_KEY")           /* automatically from local .env file! */

/* 3. CLI Arguments */
cli_list = cmd.args()

/* 4. Sleep */
cmd.sleep(1)
```

---

## 2. Net Engine (`net`)

BoseLang provides a zero-setup HTTP client for communicating with REST APIs, cloud microservices, and AI models (like Groq, OpenAI, Gemini).

### 2.1 Net Methods & Global Built-ins
Works via `net.<method>()` or globally as `get()` and `post()`:

| Method | Global Built-in | Description |
| :--- | :--- | :--- |
| `net.get(url)` | `get(url)` / `fetch(url)` | Sends HTTP GET request, returns response body string |
| `net.post(url, body, [headers])` | `post(url, body, [headers])` | Sends HTTP POST request with optional payload and header map |

### 2.2 Examples
```bose
/* GET Request */
response = net.get("https://httpbin.org/get")
out(response)

/* POST Request with JSON headers */
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_KEY"
}
body = "{\"model\": \"llama-3.3-70b-versatile\", \"messages\": [{\"role\": \"user\", \"content\": \"Hi!\"}]}"

reply = net.post("https://api.groq.com/openai/v1/chat/completions", body, headers)
out(reply)
```
