class Trie:
    def __init__(self):
        self.tree = {}

    def add(self, word):
        node = self.tree
        for letter in word:
            node = node.setdefault(letter, {})
        node['end'] = True

    def find(self, prefix):
        node = self.tree
        for letter in prefix:
            if letter not in node:
                return []
            node = node[letter]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        words = []
        if 'end' in node:
            words.append(prefix)
        for letter, child in node.items():
            if letter != 'end':
                words.extend(self._collect_words(child, prefix + letter))
        return words

def run_program():
    trie = Trie()
    while True:
        print("1. Add word\n2. Get suggestions\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            word = input("Enter word: ").strip()
            trie.add(word)
            print(f"'{word}' has been inserted.\n")
        elif choice == '2':
            prefix = input("Enter prefix: ").strip()
            suggestions = trie.find(prefix)
            print(f"Suggestions for '{prefix}': {suggestions}\n")
        elif choice == '3':
            print("exiting....")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run_program()
