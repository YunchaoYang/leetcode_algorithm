class Trie:

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        p = self
        for c in word:
            if c not in p.children:
                p.children[c] = Trie() # Create a new node if none exists.
            p = p.children[c]
        p.is_end_of_word = True


    def search(self, word: str) -> bool:
        p = self
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.is_end_of_word


    def startsWith(self, prefix: str) -> bool:
        p = self
        for c in prefix:
            if c  not in p.children:
                return False
            p = p.children[c]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()

obj.insert("apple")
param_2 = obj.search("app")
param_3 = obj.startsWith("pair")