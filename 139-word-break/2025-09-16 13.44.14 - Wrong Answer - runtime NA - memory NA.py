"""
Step 1: Create a trie and populate the trie with words from words list
Step 2: Use sliding window to check whether a a word within a given window exists in the trie
    - Keep sliding right as long as the substring within the window exists as a prefix in the trie
    - once we are able to form a word, slide the left pointer

Time O(w + s) where w is the length of words in wordDict and s is the length of input string
Space: O(w) where w is the length of the words in wordDict
"""


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word

    def has_prefix(self, prefix):
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return curr is not None

    def has_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr is not None and curr.word is not None


class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        trie = Trie()

        for word in wordDict:
            trie.add_word(word)

        curr = trie.root

        for i in range(len(s)):
            ch = s[i]

            if ch not in curr.children:
                return False

            curr = curr.children[ch]

            if curr.word:
                curr = trie.root

        return True