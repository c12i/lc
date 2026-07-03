class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        adj_list = defaultdict(list)
        for u, v in prerequisites:
            adj_list[u].append(v)
    
        def can_reach(src, target):
            visited = set()
            q = deque([src])
            while q:
                node = q.popleft()
                if node == target:
                    return True
                for neigh in adj_list[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
            return False
    
        return [can_reach(u, v) for u, v in queries]