class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        n = len(quiet)
        adj = defaultdict(list)
        indegree = [0] * n

        for u, v in richer:
            adj[u].append(v)
            indegree[v] += 1

        stack = [i for i in range(len(indegree)) if indegree[i] == 0]

        order = []

        while stack:
            node = stack.pop()
            order.append(node)

            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    stack.append(neigh)

        ans = list(range(n))

        for node in order:
            for neigh in adj[node]:
                # Fix: if node's quietest candidate is quieter than neigh's current best, update
                if quiet[ans[node]] < quiet[ans[neigh]]:
                    ans[neigh] = ans[node]
        
        return ans
