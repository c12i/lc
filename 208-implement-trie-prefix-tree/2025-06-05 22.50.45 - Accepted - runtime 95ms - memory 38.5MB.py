# how are we storing the children?
# - we would need a separate `TrieNode` class to store the charater and its children
# - how do we represent the children: mapping of [char -> adjecent TrieNode] = recursive type
# - this trie node would also contain a boolean flag to determine we are at the end of a word

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    # iterating through every character of the string/word.
    # we also keep track of the current_node -> for starters will be the self.root
    # if the char is not in the self.children map, we insert this character as the key and the value will be
    # the a new TrieNode set the current node as the newly inserted character
    # finally once iteration is complete, we set the is_end_of_word property of the the current_node as True
    def insert(self, word):
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
        leaf_node = self._traverse(word)

        return leaf_node is not None and leaf_node.is_end_of_word
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        leaf_node = self._traverse(prefix)

        return leaf_node is not None

    def _traverse(self, string):
        current_node = self.root

        for char in string:
            if char not in current_node.children:
                return None
            else:
                current_node = current_node.children[char]

        return current_node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)