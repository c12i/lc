class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_end_of_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            current_node = root
    
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in current_node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif word[i] not in current_node.children:
                    return False 
                current_node = current_node.children[word[i]]

            return current_node.is_end_of_word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)