# Hierarchical Message Decoder

A custom Python utility designed for text data manipulation and parsing. It reads unstructured data from an external `.txt` file, processes numbers and string tokens into a dictionary, and reconstructs a hidden, ordered message using algorithmic sorting logic.

## Key Features
- **File System Handling:** Efficiently reads and processes multi-line datasets using Python's built-in `with open()` file structure.
- **Robust Edge Cases:** Catches errors proactively if the target text file is completely missing or blank.
- **Data Sorting:** Implements key-value sorting to dynamically arrange scattered tokens into a coherent sentence structure.

## Setup & Run
Ensure you have a text file named `Raw_data.txt` in the same directory, then run:
```bash
python message_decoder.py
```
