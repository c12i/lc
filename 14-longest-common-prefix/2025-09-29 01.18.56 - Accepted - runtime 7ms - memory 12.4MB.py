class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.is_word = True

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        trie = Trie()
        for w in strs:
            trie.insert(w)

        curr = trie.root
        lcp = ""

        while len(curr.children.keys()) == 1 and not curr.is_word:
            key = next(iter(curr.children))
            lcp += key
            curr = curr.children[key]

        return lcp

