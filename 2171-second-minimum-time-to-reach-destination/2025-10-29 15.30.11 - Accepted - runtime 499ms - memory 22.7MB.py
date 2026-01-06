class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS: track (node, time_taken)
        # visits[node] tracks how many times we've visited with different times
        visits = defaultdict(set)
        queue = deque([(1, 0)])  # (node, current_time)
        visits[1].add(0)
        
        while queue:
            node, curr_time = queue.popleft()
            
            # calculate when we can leave this node
            # check if we're in a red light period
            cycles = curr_time // change
            if cycles % 2 == 1:  # red light (odd cycle)
                # wait
                curr_time = (cycles + 1) * change
            
            new_time = curr_time + time
            
            for neighbor in graph[node]:
                # only visit if we haven't seen this time before
                # (or have visited less than 2 times with different times)
                if new_time not in visits[neighbor] and len(visits[neighbor]) < 2:
                    visits[neighbor].add(new_time)
                    queue.append((neighbor, new_time))
        
        return max(visits[n])
