class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not len(edges):
            return [0]
            
        adj_list = defaultdict(set)

        for source, dest in edges:
            adj_list[source].add(dest)
            adj_list[dest].add(source)

        leaves = [node for node in range(n) if len(adj_list[node]) == 1]
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            next_leaves = []
            
            for leaf in leaves:
                neigh = next(iter(adj_list[leaf]))
                adj_list[neigh].discard(leaf)
                
                if len(adj_list[neigh]) == 1:
                    next_leaves.append(neigh)

            leaves = next_leaves

        return leaves
