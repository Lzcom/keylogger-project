# ⌨️ Keylogger with Timestamp

A **Python keylogger** that records every keystroke with a timestamp in a human-readable format.  
Perfect for red team labs, ethical hacking practice, or cybersecurity education.

---

## 🚀 Features

- Logs every key pressed along with a timestamp
- Distinguishes between alphanumeric and special/function keys
- Adds a session separator each time the script starts
- Exits cleanly when the **Esc** key is pressed
- Simple and lightweight — uses only the `pynput` library

---

## 🛠️ How It Works

1. Listens for keyboard events using `pynput`.
2. On every keypress, logs the key along with the current timestamp.
3. Appends to a file called `keylog.txt`.
4. Pressing `Esc` stops the logger.

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/harshit-425/keylogger-timestamp.git
   cd keylogger-timestamp
   ```

2. **Install dependencies**:
   ```bash
   pip install pynput
   ```

## ▶️ Usage

Run the script:

```bash
python keylogger.py
```
-A new session will begin with a timestamp.
-Keypresses will be recorded in keylog.txt.
-Press Esc to stop.

## 📋 Sample Output
```bash
--- New Session at 2025-04-23 14:55:10 ---
2025-04-23 14:55:12 - h
2025-04-23 14:55:13 - e
2025-04-23 14:55:14 - l
2025-04-23 14:55:14 - l
2025-04-23 14:55:15 - o
2025-04-23 14:55:17 - [Key.space]
2025-04-23 14:55:18 - w
2025-04-23 14:55:18 - o
2025-04-23 14:55:19 - r
2025-04-23 14:55:20 - l
2025-04-23 14:55:20 - d

```

## ⚠️ Disclaimer

This tool is provided for educational and authorized testing only.

-Do not use this software to monitor others without explicit consent.

-Unauthorized usage is illegal and unethical.

Use responsibly in lab environments, red team simulations, or personal testing systems.

---
## 📄 License

Licensed under the **MIT License** — free to use, modify, and share.

---

## 🤝 Contributing

Pull requests, issues, and feature suggestions are welcome!

---

## 🌐 Author

**Harshit Agrawal**

- [💼 LinkedIn](https://www.linkedin.com/in/harshit-agrawal425/)  
- [🔡 TryHackMe](https://tryhackme.com/p/harshit.agrawal425)

---

**Made with Python and a passion for cybersecurity.**

