# 🚀 Chapter 01: Getting Started

Welcome to your first step in learning **BoseLang**! In this chapter, you will learn how to run BoseLang, write your first program, and print messages to the screen.

---

## 1. What is `bose.exe`?

BoseLang runs through a single executable file named **`bose.exe`**.
- It is a **standalone program** (only ~760 KB in size).
- You do **not** need to install Python, Node.js, C++ compilers, or runtime packages.
- Whenever you want to run a BoseLang program, `bose.exe` reads your code, checks it, and executes it immediately at high speed.

---

## 2. Running Your First Script

BoseLang code files have the **`.bose`** extension (for example, `hello.bose`).

### Step 1: Create a file
Create a new text file named `hello.bose` and write the following code inside it:

```bose
/* My First BoseLang Program */
out("Hello, World!")
out("Welcome to BoseLang!")
```

### Step 2: Open Terminal / Command Prompt
Open your terminal (PowerShell, Command Prompt, or VS Code terminal) in the folder where `bose.exe` is located.

### Step 3: Run the command
Type:
```bash
.\bose.exe hello.bose
```

### Expected Output:
```text
Hello, World!
Welcome to BoseLang!
```

That's it! You have successfully written and executed your first BoseLang program.

---

## 3. The `out(...)` Function: Showing Things on Screen

In real life, when you want to tell someone something, you speak out loud. In BoseLang, when your program wants to tell the user something, it uses **`out(...)`**.

You can pass multiple items separated by commas, and BoseLang will automatically format them with a space between each item:

```bose
out("Name:", "Subhash")
out("Age:", 25)
out("Coordinates:", 100, 200, 300)
```

**Output:**
```text
Name: Subhash
Age: 25
Coordinates: 100 200 300
```

---

## 4. The `in(...)` Function: Asking the User for Input

If you want your program to ask the user a question and wait for them to type an answer, use **`in("prompt message")`**:

```bose
user_name = in("Enter your name: ")
out("Nice to meet you,", user_name)
```

When this runs:
1. It prints `Enter your name: ` on the screen.
2. It waits for the user to type something and press **Enter**.
3. It stores what the user typed in `user_name`.

---

## 5. The Golden Rule of Comments: `/* ... */`

A **comment** is a note for human readers. The computer completely ignores comments when running your program. You use comments to explain your thoughts, leave reminders, or document what your code does.

> [!IMPORTANT]
> **Golden Rule:** In BoseLang, all comments **MUST** be enclosed between `/*` and `*/`.
> 
> Single-line comments like `//` or `#` are **NOT** permitted in BoseLang.

### Examples of Valid Comments:

```bose
/* This is a single-line comment */
out("Learning comments!")

/*
   This is a multi-line comment!
   You can write as many lines as you want.
   Great for explaining complex logic.
*/
out("Done!")
```

### ❌ What NOT to do:
```bose
// This will cause a syntax error!
# This will also cause a syntax error!
```

---

## 6. Summary Checklist

Before moving to Chapter 2, make sure you understand:
- [x] BoseLang files end with `.bose`.
- [x] Run them using `.\bose.exe <filename>.bose`.
- [x] `out(...)` prints text and numbers to the screen.
- [x] `in(...)` asks the user to type something.
- [x] Comments always look like `/* your comment here */`.

Next: Learn how to store information and use data types in **[Chapter 02: Variables & Types](./02_variables_and_types.md)**!
