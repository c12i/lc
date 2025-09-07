class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = False


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefix = TrieNode()
        self.suffix = TrieNode()

        for word in words:
            curr_pref = self.prefix

            for c in word:
                if c not in curr_pref.children:
                    curr_pref.children[c] = TrieNode()
                curr_pref = curr_pref.children[c]
            curr_pref.word = True

        for word in words:
            word_rev = word[::-1]
            curr_suff = self.suffix

            for c in word_rev:
                if c not in curr_suff.children:
                    curr_suff.children[c] = TrieNode()
                curr_suff = curr_suff.children[c]

        

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        if self.startsWith(pref) and self.endsWith(suff):
            return 0
        return -1

    
    def startsWith(self, pref):
        curr = self.prefix

        for c in pref:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr is not None

    
    def endsWith(self, suff):
        curr = self.suffix

        for c in suff:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr is not None
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)