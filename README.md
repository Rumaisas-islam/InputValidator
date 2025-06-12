# InputValidator 🛡️

A simple Python class that validates usernames based on specific rules such as:

- ✅ Must be alphanumeric (no spaces or special characters)
- ❌ Should not contain banned words like `admin` or `root`
- ❌ Should not end with restricted endings like `123` or `000`
- 📏 Minimum length: 5 characters

This project is useful for learning basic input validation and object-oriented programming in Python.

---

## How It Works

When you run the script, it will:

1. Ask the user to enter a username.
2. Validate the input using a set of conditions.
3. Print whether the username is valid or show specific error messages.

---

## Example Output

```
Enter your username: admin123
❌ Invalid Username
→Username should not end with '123' or '000'.
Username should not contain 'admin' or 'root'.
```

---

## Run the Script

```bash
python input_validator.py
```

---

## License

This project is open-source and free to use.
