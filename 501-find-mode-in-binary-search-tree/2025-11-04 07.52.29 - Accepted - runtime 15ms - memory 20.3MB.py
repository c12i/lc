class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        
        # first pass: find max frequency
        self.prev_val = None
        self.counter = 0
        self.max_freq = 0
        
        def dfs1(node):
            if not node:
                return
            dfs1(node.left)
            if node.val == self.prev_val:
                self.counter += 1
            else:
                self.max_freq = max(self.max_freq, self.counter)
                self.counter = 1
            self.prev_val = node.val
            dfs1(node.right)
        
        dfs1(root)
        # handle last group
        self.max_freq = max(self.max_freq, self.counter)
        
        # second pass: collect all values with max frequency
        self.prev_val = None
        self.counter = 0
        self.result = []
        
        def dfs2(node):
            if not node:
                return
            dfs2(node.left)
            if node.val == self.prev_val:
                self.counter += 1
            else:
                if self.counter == self.max_freq:
                    self.result.append(self.prev_val)
                self.counter = 1
            self.prev_val = node.val
            dfs2(node.right)
        
        dfs2(root)
        # handle last group
        if self.counter == self.max_freq:
            self.result.append(self.prev_val)
        
        return self.result