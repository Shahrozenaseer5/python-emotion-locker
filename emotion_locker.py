"""
Emotion Locker - Personal Thought Encryption Notebook

Author: Shahroze
Date: 5 May 2026
Project Type: CLI Application (Python)

Description:
Emotion Locker is a personal journaling system that encrypts user thoughts using a custom rule-based encoding mechanism.
It allows users to store, retrieve, decode, and analyze emotional entries in a secure and structured format.

Core Features:
- Custom text encryption and decryption system
- Emotion-based journal storage
- Persistent data storage using JSON
- Entry search, deletion, and analytics
- Fully CLI-based interactive experience

Concepts Used:
- File Handling (JSON read/write)
- String manipulation and encoding logic
- Functions and modular programming
- Dictionaries for analytics
- Exception handling
- CLI menu system

Note:
This project is built for learning purposes to strengthen Python fundamentals and problem-solving skills.
"""
"""
1. The “Emotion Locker” — Personal Thought Encryption Notebook
You type your thoughts.
The program converts them into a custom encrypted pattern using rules you design.
Later you can decrypt them using your own key.
Core skills:
•	File handling
•	Functions
•	Dictionaries for mapping
•	Your own encoding-decoding logic

Encoding Rules :
Rule 1 - Length-based decision
- If word length ≥ 4 → apply transformation
- If word length < 4 → simple reverse

Rule 2 - Rotate characters
- Move first 2 characters to the end

Rule 3 - Add fixed markers (not random)
- Add 2 known prefix + 2 known suffix characters

Rule 4 - Shift characters (light encryption)
- Shift each letter by +1 in ASCII (or alphabet)

Decoding Rules :
Rule 1 - Reverse shift
- Shift each character -1

Rule 2 - Remove known markers
- Remove first 2 and last 2 characters

Rule 3 - Restore rotation
- Move last 2 characters to the beginning

Rule 4 - Handle short words
- If length < 4 → reverse again
"""
import json
from datetime import datetime

file_name = "emotion_locker.json"
prefix = "xy"
suffix = "cd"
# move letters forward by 1 (a->b->c)
def shift_forward(text):
    result = []
    for ch in text:
        if ch.islower():
            result.append(chr((ord(ch) - ord('a') + 1) % 26 + ord('a')))
        elif ch.isupper():
            result.append(chr((ord(ch) - ord('A') + 1) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)

# move letters backward by 1 (c->b->a)
def shift_backward(text):
    result = []
    for ch in text:
        if ch.islower():
            result.append(chr((ord(ch) - ord('a') - 1) % 26 + ord('a')))
        elif ch.isupper():
            result.append(chr((ord(ch) - ord('A') - 1) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)

# Encoding
def encode(text):
    words = text.split()
    result_words = []
    for w in words:
        if len(w) < 4:
            result_words.append(w[::-1])
        else:
            rotated = w[2:] + w[:2]
            modified = prefix + rotated + suffix
            result_words.append(shift_forward(modified))
    return " ".join(result_words)
# Decoding
def decode(text):
    words = text.split()
    result_words = []
    for w in words:
        if len(w) < 4:
            result_words.append(w[::-1])
        else:
            step_1 = shift_backward(w)
            if not (step_1.startswith(prefix) and step_1.endswith(suffix)):
                result_words.append(w)
                continue
            step_2 = step_1[len(prefix):-len(suffix)]
            result_words.append(step_2[-2:] + step_2[:-2])
    return " ".join(result_words)
# save encoded message
def save_entry(emotion, encoded_text):
    date = datetime.now().strftime("%Y-%m-%d")
    entry = {
        "date": date,
        "emotion": emotion,
        "message": encoded_text
    }
    try :
      with open(file_name, 'r') as f:
        data = json.load(f)
    except (FileNotFoundError,  json.JSONDecodeError):
        data = []
    data.append(entry)
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
# view all entries
def view_entries() :
    try :
        with open(file_name, 'r') as f :
            data = json.load(f)
            if not data :
                print('No entry found !')
                return
            for i, item in enumerate(data, 1):
                decoded_preview = decode(item['message'])
                print(f"{i}. {item['date']} | {item['emotion']} | {decoded_preview}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("File missing or corrupted.")
        return

# Decode selected entry
def decode_entry():
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
            if not data:
                print("No entries to decode!")
                return
            for i, item in enumerate(data, 1):
                print(f"{i}. {item['date']} | {item['emotion']}")
            choice = int(input("Select entry number to decode: "))

            if choice < 1 or choice > len(data):
                print("Invalid selection.")
                return

            encoded_text = data[choice - 1]['message']
            decoded_text = decode(encoded_text)
            print("Decoded message:", decoded_text)

    except ValueError:
        print("Invalid input.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("File missing or corrupted.")
        return

# Search entries by emotion
def search_by_emotion():
    try :
        with open(file_name, 'r') as f:
            data = json.load(f)
        if not data:
            print("No entries found!")
            return
        target = input('Enter emotion to search :').strip().lower()
        found = False
        for i, item in enumerate(data, 1):
            if item['emotion'].lower() == target:
                decoded_preview = decode(item['message'])
                print(f"{i}. {item['date']} | {item['emotion']} | {decoded_preview}")
                found = True
        if not found:
           print("No matching entries found.")

    except (FileNotFoundError, json.JSONDecodeError):
        print("File missing or corrupted.")
        return

# delete an entry
def delete_entry():
    try :
        with open(file_name, 'r') as f:
            data = json.load(f)
        if not data:
           print("No entries to delete.")
           return
        for i, item in enumerate(data, 1):
            print(f"{i}. {item['date']} | {item['emotion']}")
        try :
            choice = int(input("Select entry number to delete: "))
        except ValueError:
           print("Invalid input.")
           return
        if choice < 1 or choice > len(data):
           print("Invalid selection.")
           return
        confirm = input("Are you sure? (yes/no): ").lower()
        if confirm != "yes":
           print("Deletion cancelled.")
           return
        deleted = data.pop(choice - 1)
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Deleted entry: {deleted['emotion']} on {deleted['date']}")

    except (FileNotFoundError, json.JSONDecodeError):
        print("File missing or corrupted.")
        return

# Emotion Analytics
def emotion_analytics():
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
        if not data:
            print('No entries found!')
            return
        counts = {}
        for item in data:
            emotion = item['emotion']
            counts[emotion] = counts.get(emotion, 0) + 1
        print("\nEmotion Statistics:")
        for emotion, count in counts.items():
            print(f"{emotion}: {count}")

    except (FileNotFoundError, json.JSONDecodeError):
        print("File missing or corrupted.")
        return
# Main loop
def main():
   while True:
       print("\n=== Emotion Locker ===")
       print("1. Add new emotion")
       print("2. View entries")
       print("3. Decode entry")
       print("4. Search by emotion")
       print("5. Delete entry")
       print("6. Show analytics")
       print("7. Exit")

       choice = input("Choose an option: ").strip()

       if choice == "1":
           emotion = input("Enter emotion (happy/sad/etc): ").strip()
           message = input("Enter your message: ").strip()

           encoded_text = encode(message)
           save_entry(emotion, encoded_text)

           print("Saved successfully.")

       elif choice == "2":
           view_entries()

       elif choice == "3":
           decode_entry()

       elif choice == "4":
           search_by_emotion()

       elif choice == "5":
           delete_entry()

       elif choice == "6":
           emotion_analytics()

       elif choice == "7":
           print('Exiting...')
           break

       else:
           print("Invalid choice.")
# Entry point
if __name__ == "__main__":
    main()