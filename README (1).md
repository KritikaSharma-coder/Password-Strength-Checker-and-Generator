# Password Strength Checker + Generator

A simple command-line Python program that checks how strong a password is
and can generate a new strong password for you.

## Features

- **Check a password** — scores it out of 5 based on length, uppercase,
  lowercase, numbers, and symbols, and gives tips to improve it.
- **Detects common passwords** — things like `123456` or `password` are
  instantly flagged as very weak.
- **Generate a strong password** — creates a random password of any length
  you choose, guaranteed to include uppercase, lowercase, a number, and a
  symbol.

## How to run it

You need Python 3 installed. No extra libraries are required.

```bash
python password_tool.py
```

Then choose an option from the menu:

```
===== PASSWORD TOOL =====
1. Check a password
2. Generate a strong password
3. Exit
```

## Example

```
Choose an option (1-3): 1
Enter a password to check: Hello123!

Strength: Very Strong  (5/5)
Great password!
```

```
Choose an option (1-3): 2
How long should the password be? (min 6): 12

Generated password: gSog%BzQ16lO
Strength: Very Strong  (5/5)
```

## How the strength score works

| Score | Label |
|-------|-------|
| 0 - 1 | Very Weak |
| 2     | Weak |
| 3     | Medium |
| 4     | Strong |
| 5     | Very Strong |

One point is added for each of: length of 8+, a lowercase letter, an
uppercase letter, a number, and a symbol. Common passwords are always
scored 0, regardless of the rules above.

## Concepts used

- Strings and loops (checking each character of the password)
- Functions (one for checking, one for generating)
- if / elif / else
- Lists
- The `random` and `string` modules

## Project files

| File | Purpose |
|------|---------|
| `password_tool.py` | The program |
| `README.md` | This file |
