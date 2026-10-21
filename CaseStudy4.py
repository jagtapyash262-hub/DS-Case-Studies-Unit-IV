
# Case Study 4: Dictionary Application Using Hash Tables

class Dictionary:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, word):
        return sum(ord(char) for char in word.lower()) % self.size

    # Add a word and its meaning
    def add_word(self, word, meaning):
        index = self.hash_function(word)

        # Update meaning if word already exists
        for entry in self.table[index]:
            if entry[0] == word.lower():
                entry[1] = meaning
                print(f"Meaning updated for '{word}'.")
                return

        # Separate chaining handles collisions
        self.table[index].append([word.lower(), meaning])
        print(f"Word '{word}' added successfully.")

    # Search for a word
    def search_word(self, word):
        index = self.hash_function(word)

        for entry in self.table[index]:
            if entry[0] == word.lower():
                print(f"Meaning of '{word}': {entry[1]}")
                return

        print(f"Word '{word}' not found in dictionary.")

    # Display all dictionary entries
    def display(self):
        print("\nDictionary Contents:")

        for index, bucket in enumerate(self.table):
            if bucket:
                for word, meaning in bucket:
                    print(f"Index {index}: {word} - {meaning}")


# Main program
dictionary = Dictionary()

print("DICTIONARY APPLICATION USING HASH TABLES\n")

dictionary.add_word("cat", "A small domesticated animal")
dictionary.add_word("act", "To do something")
dictionary.add_word("dog", "A domesticated animal")
dictionary.add_word("god", "A divine being")
dictionary.add_word("apple", "A fruit")

print("\nSearching Words:")
dictionary.search_word("cat")
dictionary.search_word("act")
dictionary.search_word("bird")

dictionary.display()
