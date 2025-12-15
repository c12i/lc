class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.word = word         

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ROWS, COLS = len(board), len(board[0])

        result = []
        visited = set()
        trie = Trie()

        for word in words:
            trie.add_word(word)

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def dfs(r, c, node):
            if (
                r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visited
            ):
                return

            ch = board[r][c]
            if ch not in node.children:
                return

            next_node = node.children[ch]
            if next_node.word:
                result.append(next_node.word)
                next_node.word = None

            visited.add((r, c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, next_node)

            visited.remove((r, c))

            # back-pruning - needed this for TLE
            if not next_node.children and next_node.word is None:
                del node.children[ch]


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root)

        return result
