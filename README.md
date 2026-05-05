# Emotion Locker - Personal Thought Encryption Notebook

A Python-based CLI (Command Line Interface) application that allows users to store, encrypt, and manage personal thoughts using a custom rule-based encoding system.

---

## Overview

**Emotion Locker** is a journaling system where each entry is encrypted using custom-designed logic. It enables users to securely store emotional thoughts and later retrieve or decode them when needed.

This project focuses on strengthening Python fundamentals, file handling, and logical problem-solving.

---

## Features

- ✍️ Add emotional journal entries  
- 🔐 Custom encryption & decryption system  
- 📂 Persistent storage using JSON  
- 🔍 Search entries by emotion  
- 🗑️ Delete specific entries  
- 📊 Emotion analytics  
- 🖥️ Interactive command-line interface  

---

## How Encryption Works

The encoding system applies multiple transformations:

### For words with length ≥ 4
- Rotate first 2 characters to the end  
- Add prefix ('xy') and suffix ('cd')  
- Apply ASCII shift (+1)  

### For words with length < 4
- Simply reversed  

Decryption reverses the exact process.

---

## Tech Stack

- Python 3  
- JSON (for storage)  
- Built-in libraries: datetime, json  

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/emotion-locker.git
```

2. Navigate to the project folder:
```bash
cd emotion-locker
```

3. Run the script:
```bash
python emotion_locker.py
```

## 📂 Project Structure
```text
emotion-locker/
│
├── emotion_locker.py
├── emotion_locker.json   # auto-generated storage file
└── README.md
```

## Example Use Case
- User enters a thought: "I am happy today"
- System encrypts and stores it

Later, the user can:

- View decoded preview
- Search by emotion (happy, sad, etc.)
- Analyze emotional patterns

## Learning Outcomes

This project demonstrates:

- Strong understanding of Python fundamentals
- Logical thinking for custom encoding system
- File-based data persistence
- CLI application design
- Clean and modular coding practices

## Future Improvements
- Password-protected encryption key
- GUI version (Tkinter or Streamlit)
- Cloud-based storage integration
- Stronger encryption algorithm (AES-based)

## Author
**Shahroze**
Aspiring AI/ML Engineer | Python Developer in Progress
