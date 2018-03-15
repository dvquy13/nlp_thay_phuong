class TrieNode():
    def __init__(self, char):
       self.char = char
       self.children = []
       self.is_finished_word = False
       self.counter = 0

class Trie():
    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):
        node = self.root
        for i in range(len(word)):
            found_in_child = False
            char = word[i]
            for child in node.children:
                if child.char == char:
                    if i == len(word)-1:
                        if child.is_finished_word:
                            child.counter += 1
                        else:
                            child.is_finished_word = True
                            child.counter = 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                if i == len(word)-1:
                    new_node.is_finished_word = True
                    new_node.counter = 1
                node.children.append(new_node)
                node = new_node
        return node

    def __getitem__(self, word):
        node = self.root
        for i in range(len(word)):
            found_in_child = False
            char = word[i]
            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    if i == len(word)-1 and child.is_finished_word:
                        return child.counter
                    break
            if not found_in_child:
                return 0

def test():
    trie = Trie()
    trie.add('abc')
    assert trie['abc'] == 1
    assert trie['ab'] == 0

if __name__ == '__main__':
    test()
