
# Data-Structure-Unit-4-Case-Study

A Python case study demonstrating a Dictionary Application using Hash Tables with collision resolution.

# Dictionary Application Using Hash Tables

A dictionary application stores words and their meanings and allows users to search for a word efficiently.

This case study demonstrates how hashing can be used to store and retrieve words and meanings. It uses a hash table and separate chaining to handle collisions when multiple words map to the same index.

## Features

- Store words and their meanings.
- Calculate hash-table indexes using a hash function.
- Search for a word and display its meaning.
- Handle collisions using separate chaining.
- Update the meaning of an existing word.
- Display all stored dictionary entries.
- Display a message when a word is not found.

## Data Structure Used

**Hash Table**

A hash table stores data as key-value pairs. A hash function converts each word into an index in the table.

In this application:
- The word acts as the key.
- The meaning acts as the value.
- The hash function calculates the storage index.
- Each index contains a list that stores entries with the same hash index.

## Collision Resolution Technique

**Separate Chaining**

A collision occurs when two different words produce the same hash-table index.

This program handles collisions using separate chaining. Each table index contains a list of entries, allowing multiple words to be stored at the same index.

For example, the words `cat` and `act` produce the same hash value with the hash function used in this program. Both words are stored in the same bucket.

## Hash Function

The program calculates the index using the following formula:

```text
Hash Index = Sum of character codes % Table Size
```

The program converts words to lowercase before calculating the hash value, making searches case-insensitive.

## Requirements

- Python 3.7 or newer
- No external packages are required.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python CaseStudy4.py
   ```

If your system uses `python3`, run:

   ```bash
   python3 CaseStudy4.py
   ```

## Sample Output

See `sample_output.txt` for the complete program output.

```text
DICTIONARY APPLICATION USING HASH TABLES

Word 'cat' added successfully.
Word 'act' added successfully.
Word 'dog' added successfully.
Word 'god' added successfully.
Word 'apple' added successfully.

Searching Words:
Meaning of 'cat': A small domesticated animal
Meaning of 'act': To do something
Word 'bird' not found in dictionary.
```

## Time Complexity

Let `n` be the number of stored words and `m` be the number of hash-table buckets.

- Hash function calculation: O(k), where k is the word length.
- Insertion: O(1) average expected bucket work, excluding hashing; O(n) worst case.
- Search: O(1) average expected bucket work, excluding hashing; O(n) worst case.
- Display all entries: O(m + n).
- Space Complexity: O(m + n).

Performance depends on the hash function and how evenly entries are distributed across buckets.

## Advantages

- Supports efficient average-case word lookup.
- Handles collisions using separate chaining.
- Allows existing meanings to be updated.
- Can store many word-meaning pairs.
- Demonstrates an important hashing technique.

## Limitations

- Different words can produce the same hash index.
- A poor hash function can cause many collisions.
- Worst-case search and insertion can take linear time.
- This demonstration uses a fixed-size hash table and does not implement automatic resizing.

## Applications

- Dictionary applications.
- Spell-checking systems.
- Contact lookup systems.
- Symbol tables in compilers.
- Word databases and lookup applications.

## Conclusion

This case study demonstrates how a dictionary can be implemented using a hash table in Python.

The hash function maps words to table indexes, and separate chaining handles collisions by storing multiple entries in the same bucket.

Hash tables provide efficient average-case lookup when the hash function distributes entries well.

## Files Included

- `CaseStudy4.py` - Python source code.
- `sample_output.txt` - Sample program output.
- `README.md` - Case study documentation.

