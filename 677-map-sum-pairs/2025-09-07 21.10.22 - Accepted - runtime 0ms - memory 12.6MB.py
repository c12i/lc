class TrieNode(object):
    def __init__(self, value = None):
        self.children = {}
        self.word = False
        self.value = value


class MapSum(object):

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        curr = self.root
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True
        curr.value = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]

        q = deque([curr])
        sums = 0

        while q:
            node = q.popleft()

            if node.word:
                sums += node.value
            for c in node.children.values():
                q.append(c)

        return sums

        # def dfs(node):
        #     if not node:
        #         return 0
        #     total = node.value if node.word else 0
        #     for child in node.children.values():
        #         total += dfs(child)
        #     return total
            
        # return dfs(curr)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)