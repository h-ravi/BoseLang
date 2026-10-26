# Chapter 16: Level 9 Native Web Server Engine (`web`)

> **"Zero External Dependencies, Zero Boilerplate, Pure Human-Friendly Ergonomics."**

BoseLang Level 9 introduces the built-in `web` module. It turns BoseLang into a high-performance HTTP server capable of serving static frontend websites (HTML/CSS/JS) and RESTful JSON APIs in pure safe Rust standard library with zero external packages.

---

## 1. Quick Taste: 1-Line Full Website Hosting

If you have a website folder (`public/` or `dist/` containing `index.html`, `style.css`, `app.js`, images):

```bose
/* Direct initialization with live reload */
fix server = web(8080, true)
out("⚡ Website live at: http://localhost:8080")

loop req from server {
    req.static("public")
}
```

* Visiting `http://localhost:8080/` $\rightarrow$ automatically serves `public/index.html`.
* Requesting `/style.css` $\rightarrow$ serves `public/style.css` with `Content-Type: text/css; charset=utf-8`.
* Requesting `/app.js` $\rightarrow$ serves with `Content-Type: application/javascript; charset=utf-8`.
* Requesting `/logo.png` $\rightarrow$ serves binary image with `Content-Type: image/png`.
* Missing files automatically return clean `404 Not Found`.

---

## 2. Server Initialization & Ergonomics

You can launch a server directly using `web(...)` with flexible, human-friendly parameter styles:

### A. Positional Arguments: `web(port, [host], [live])`

| Syntax | Port | Host Address | Live Reload | Description |
| :--- | :---: | :---: | :---: | :--- |
| `web(8080)` | 8080 | `127.0.0.1` | `false` | Default private host, static mode |
| `web(8080, true)` | 8080 | `127.0.0.1` | `true` | Shorthand for local development with auto-reload |
| `web(8080, "public")` | 8080 | `0.0.0.0` | `false` | Accessible across LAN/Wi-Fi hotspot |
| `web(8080, public, true)` | 8080 | `0.0.0.0` | `true` | Public LAN host with live reload |
| `web(8080, private, false)` | 8080 | `127.0.0.1` | `false` | Explicit private localhost |

> **Host Alias Mapping:**
> * `"private"`, `"localhost"`, or `private` $\rightarrow$ `127.0.0.1` (Only your computer can access)
> * `"public"`, `"all"`, `"lan"`, or `public` $\rightarrow$ `0.0.0.0` (Shareable with mobile/devices on same Wi-Fi/Hotspot)

### B. Named / Map Configuration Style

Keys can be passed in any order:

```bose
/* Map configuration */
fix server = web({
    "port": 8080,
    "host": "public",
    "live": true
})
```

---

## 3. Automatic Live Reloading (`live: true`)

When `live: true` is enabled:
1. **File Watcher**: BoseLang monitors your `.bose` script file for any edits or saves.
2. **Instant Hot-Reload**: As soon as you save your file in VS Code or any editor, BoseLang seamlessly drops the port, restarts the server, and prints:
   ```text
   ⚡ [live] Change detected in 'main.bose'. Hot-reloading server...
   ```
3. **Automatic Browser Refresh**: Served HTML pages automatically include a lightweight EventSource listener (`/__bose_live__`). When the server reloads, open browser tabs refresh automatically without pressing `Ctrl+R` or touching the browser!

---

## 4. Modern Full-Stack App: Static Frontend + REST APIs

```bose
fix app = web(8080, true)
out("⚡ Server running at http://localhost:8080")

loop req from app {
    /* 1. REST API: GET all users */
    when req.path == "/api/users" and req.method == "GET" {
        users = [
            {"id": 1, "name": "Ranjeet", "role": "Architect"},
            {"id": 2, "name": "Subhash", "role": "Developer"}
        ]
        req.cors().json(users)
    }

    /* 2. REST API: POST create user */
    again req.path == "/api/users" and req.method == "POST" {
        payload = req.body
        when payload == Null or payload["name"] == Null {
            req.status(400).json({"error": "Name field is required"})
        } otherwise {
            out("Saved new user:", payload["name"])
            req.status(201).json({
                "message": "User created successfully",
                "data": payload
            })
        }
    }

    /* 3. Query Parameter Search: /search?q=boselang&limit=5 */
    again req.path == "/search" {
        query = req.query["q"]
        limit = int(req.query["limit"])
        req.json({
            "query": query,
            "limit": limit,
            "results": ["BoseLang", "Rust", "Netaji"]
        })
    }

    /* 4. Frontend Website Fallback */
    otherwise {
        req.static("public")
    }
}
```

---

## 5. WebServer Methods Reference

Any variable holding the WebServer instance (e.g. `fix server = web(8080)`):

| Method | Description |
| :--- | :--- |
| `server.port()` | Returns the bound port number (`8080`). |
| `server.host()` | Returns the bound host IP (`"127.0.0.1"` or `"0.0.0.0"`). |
| `server.live()` | Returns whether live reload is enabled (`true`/`false`). Can also be called to activate live reload on an existing server. |
| `server.cors()` | Enables global permissive CORS for all requests. |
| `server.next()` | Manually polls and retrieves the next incoming `Request` (or `Null` if none). |
| `server.stop()` | Gracefully stops the HTTP listener. |

---

## 6. The Request (`req`) Object Reference

Every iteration of `loop req from server` yields an immutable `Request` object:

| Property | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `req.method` | `text` | Uppercase HTTP Method | `"GET"`, `"POST"`, `"PUT"`, `"DELETE"` |
| `req.path` | `text` | Clean URL Path without query | `"/api/users"`, `"/"` |
| `req.url` | `text` | Full URL Path with query | `"/search?q=bose&page=1"` |
| `req.query` | `map` | URL Decoded Query Parameters | `{"q": "bose", "page": "1"}` |
| `req.headers`| `map` | Lowercase Request Headers | `{"content-type": "application/json"}` |
| `req.cookies`| `map` | Parsed incoming browser cookies | `{"session": "xyz123", "theme": "dark"}` |
| `req.params` | `list` | List of URL path segments | `["users", "105", "profile"]` |
| `req.body` | `any` | Auto-parsed JSON map/list or text | `{"name": "Subhash"}` |
| `req.raw_body`| `text` | Raw unparsed body text | `'{"name":"Subhash"}'` |
| `req.ip` | `text` | Client IP Address | `"127.0.0.1"` |

---

## 7. Response & Helper Methods (Fluent Chaining)

All response methods support fluent method chaining:

| Method | Description |
| :--- | :--- |
| `req.send(text_or_html)` | Sends HTML or plain text response with correct `Content-Type`. Injects live reload script when `live: true`. |
| `req.json(data)` | Serializes native map/list/primitive into JSON with `Content-Type: application/json`. |
| `req.file(filepath)` | Reads local file with automatic MIME detection. |
| `req.static(folder, [opts])` | Hosts static directory (`folder`) with automated MIME lookups and Clean URLs (`/about` -> `about.html`). Set `{"clean": false}` to disable clean URLs, or `{"spa": true}` for SPA fallback. |
| `req.spa(folder)` | Dedicated SPA hosting: serves static files; for any non-existent route, serves `index.html`. |
| `req.cookie(name, val, [opts])` | Sets `Set-Cookie` header with optional map (`max_age`, `http_only`, `same_site`). |
| `req.clear_cookie(name)` | Clears a cookie on client browser (`Max-Age=0`). |
| `req.match(pattern)` | Matches URL against pattern (`"/users/:id"`). Returns map `{"id": "..."}` or `Null`. |
| `req.param(index)` | Returns n-th path segment (e.g. `req.param(0) -> "users"`). Supports negative index. |
| `req.status(code)` | Sets status code (`200`, `201`, `400`, `404`, `500`). Chaining: `req.status(404).send(...)`. |
| `req.header(key, val)` | Adds custom HTTP header: `req.header("X-Powered-By", "BoseLang")`. |
| `req.cors()` | Attaches permissive CORS headers and auto-handles OPTIONS preflight with 204. |
| `req.redirect(url, [code])`| Sends HTTP 302/301 redirection header. |
| `req.download(path, [name])`| Sends file with `Content-Disposition: attachment`. |

---

## 8. Advanced Features: Clean URLs, SPA, Cookies & Dynamic Routing

These features are ready whenever you need them:

### A. Clean URLs (Automatic Extension-less Routing)
In modern web design, URLs should be clean and professional (`/about`) instead of exposing file extensions (`/about.html`).

In BoseLang, **Clean URLs are enabled by default** when using `req.static()`:
```bose
/* Serves pages folder with automated Clean URLs */
req.static("pages")
```

If your `pages/` directory has:
```text
pages/
├── index.html
├── about.html
├── contact.html
└── style.css
```

- When a visitor opens `/` -> serves `pages/index.html`
- When a visitor opens `/about` -> automatically resolves and serves `pages/about.html`!
- When a visitor opens `/contact` -> automatically resolves and serves `pages/contact.html`!
- When a visitor opens `/about.html` -> explicitly still serves `pages/about.html`!
- Non-HTML assets (like `/style.css`, `/logo.png`) are served directly with proper MIME headers.

**Disabling Clean URLs (Strict Extension Mode):**
If you want strict URLs that only serve exact file paths without the `.html` fallback:
```bose
/* Disables Clean URLs (e.g. /about will return 404 unless /about.html is explicitly typed) */
req.static("pages", {"clean": false})
// or concisely:
req.static("pages", false)
```

### B. Single Page Applications (SPA) Guide: React, Vue, Svelte & Vite

In modern web development, Single Page Applications (React, Vue, Svelte, Angular, Solid) handle page navigation entirely in the browser using client-side routing (e.g. `react-router-dom`, `vue-router`). 

#### 1. The SPA Routing Challenge
* When a visitor opens `http://localhost:8080/`, BoseLang serves `index.html`.
* Inside the browser, when the user clicks a link to `/about` or `/dashboard`, the frontend router changes the page instantly without a full browser reload.
* **The Problem:** If the user presses `F5` / `Ctrl+R` (hard refresh) or directly enters `http://localhost:8080/dashboard` in the browser address bar, a traditional web server looks for a physical file named `/dashboard.html` or `/dashboard/index.html`. Since it does not exist, the server crashes with a `404 Not Found` error.

#### 2. The Solution: `req.spa("folder")`
BoseLang's `req.spa()` provides an intelligent two-tier router:
1. **Static Asset Resolution:** If the browser requests a real static file that exists on disk (e.g. `/assets/index-abc.js`, `/style.css`, `/logo.png`, `/favicon.ico`), BoseLang serves it immediately with high-performance MIME headers.
2. **Client Route Fallback:** If the browser requests any non-existent route (e.g. `/about`, `/users/42`, `/settings/billing`), BoseLang automatically falls back to serving `index.html` with HTTP 200. The frontend router boots up in the browser, reads `window.location.pathname`, and renders the correct view seamlessly!

---

#### 3. Step-by-Step Project Walkthrough

##### Step 1: Recommended Project Structure
You can keep your frontend framework in a subfolder (e.g. `frontend/`) and your BoseLang backend at the root:

```text
my_fullstack_app/
├── frontend/                  /* React / Vue / Vite project */
│   ├── src/
│   │   ├── App.jsx            /* React Router components */
│   │   └── main.jsx
│   ├── package.json
│   └── dist/                  /* Created after running: npm run build */
│       ├── index.html
│       └── assets/
│           ├── index-d7b1a2.js
│           └── index-c4a8b1.css
└── main.bose                  /* BoseLang Backend Server */
```

##### Step 2: Build the Frontend
Inside your frontend directory, run your framework build tool:
```bash
cd frontend
npm run build
```
This compiles your React/Vue code and bundles it into `frontend/dist/`.

##### Step 3: Write the BoseLang Full-Stack Server (`main.bose`)
BoseLang handles both your REST API and your SPA in a single, elegant loop:

```bose
/* Initialize server with live reload */
fix server = web(8080, true)
out("🚀 Full-Stack App live at: http://localhost:8080")

loop req from server {
    /* 1. REST API Endpoints (Handled directly by BoseLang) */
    when req.path == "/api/todos" and req.method == "GET" {
        todos = [
            {"id": 1, "title": "Setup BoseLang Server", "completed": true},
            {"id": 2, "title": "Build React Frontend", "completed": true},
            {"id": 3, "title": "Deploy to Production", "completed": false}
        ]
        req.json(todos)
    }

    again req.path == "/api/todos" and req.method == "POST" {
        payload = req.body
        when payload == Null or payload["title"] == Null {
            req.status(400).json({"error": "Title is required"})
        } otherwise {
            out("⚡ Added new todo:", payload["title"])
            req.status(201).json({
                "message": "Todo created successfully",
                "item": payload
            })
        }
    }

    /* 2. All other routes: Fallback to React/Vue SPA */
    otherwise {
        req.spa("frontend/dist")
    }
}
```

##### Step 4: Consume BoseLang API from React
Because BoseLang serves both your React frontend and your backend REST APIs on the **exact same port (`8080`)**, you **never run into CORS errors** in production. Your React components can call the API using relative paths:

```jsx
// React / Vue Component
import { useEffect, useState } from "react";

export function TodoList() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    // Direct call to BoseLang backend on the same origin!
    fetch("/api/todos")
      .then((res) => res.json())
      .then((data) => setTodos(data));
  }, []);

  return (
    <div>
      <h2>My Tasks</h2>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </div>
  );
}
```

---

#### 4. Alternative: Lightweight Micro-SPA (No React / Zero-NPM)
If you do not want to use React or Node.js, you can achieve the exact same "no-reload / seamless page transition" in plain HTML using a tiny 10-line client script:

```html
<!-- In public/index.html -->
<nav>
  <a href="/" onclick="nav(event, '/')">Home</a>
  <a href="/about" onclick="nav(event, '/about')">About</a>
</nav>

<div id="app">Welcome to Home!</div>

<script>
  async function nav(e, path) {
    e.preventDefault(); // Stop full browser reload
    const res = await fetch(path + '?partial=1');
    document.getElementById('app').innerHTML = await res.text();
    window.history.pushState({}, '', path); // Update browser URL
  }
  window.onpopstate = () => nav({ preventDefault: () => {} }, location.pathname);
</script>
```

### C. Cookies for Login & Settings
Read incoming cookies or send new ones:
```bose
/* 1. Set cookie on login */
when req.path == "/login" {
    req.cookie("session", "token_12345", {"max_age": 86400, "http_only": true})
       .send("Login successful!")
}

/* 2. Read cookie on protected page */
again req.path == "/dashboard" {
    token = req.cookies["session"]
    when token == Null {
        req.status(401).send("Please login first")
    } otherwise {
        req.send("Welcome! Session: " + token)
    }
}

/* 3. Logout */
again req.path == "/logout" {
    req.clear_cookie("session").send("Logged out")
}
```

### D. Dynamic Route Parameters (`req.match` & `req.params`)
Extract variables directly from URLs without complex parsing:
```bose
/* Match /users/:id */
matched = req.match("/users/:id")
when matched != Null {
    user_id = matched["id"]
    req.json({"user": user_id})
}

/* Or read raw URL segments directly */
/* If path is /products/electronics/laptop */
first_part = req.param(0)   /* "products" */
last_part = req.param(-1)   /* "laptop" */
```

---

## 9. Built-in MIME Registry

Zero-allocation automatic MIME resolution:

* `.html`, `.htm` $\rightarrow$ `text/html; charset=utf-8`
* `.css` $\rightarrow$ `text/css; charset=utf-8`
* `.js`, `.mjs` $\rightarrow$ `application/javascript; charset=utf-8`
* `.json` $\rightarrow$ `application/json; charset=utf-8`
* `.png` $\rightarrow$ `image/png`
* `.jpg`, `.jpeg` $\rightarrow$ `image/jpeg`
* `.gif` $\rightarrow$ `image/gif`
* `.svg` $\rightarrow$ `image/svg+xml`
* `.ico` $\rightarrow$ `image/x-icon`
* `.webp` $\rightarrow$ `image/webp`
* `.woff2` $\rightarrow$ `font/woff2`
* `.wasm` $\rightarrow$ `application/wasm`
* `.pdf` $\rightarrow$ `application/pdf`
* `.txt` $\rightarrow$ `text/plain; charset=utf-8`

---

## 10. Security Shields

1. **Directory Traversal Attack Prevention:**
   Malicious client requests containing `..` or drive separators (e.g. `GET /../../Windows/System32/calc.exe` or `GET /../../../etc/passwd`) are automatically intercepted and return `403 Forbidden`.
2. **Capability Security:**
   Restrict server powers on untrusted modules:
   ```bose
   fix static_app = web(static) /* Only static file serving granted */
   fix server_app = web(server) /* Only server listening granted */
   ```
