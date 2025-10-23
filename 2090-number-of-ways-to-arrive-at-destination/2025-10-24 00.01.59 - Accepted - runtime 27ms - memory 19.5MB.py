class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        
        # Build adjacency list
        adjList = defaultdict(list)
        for u, v, time in roads:
            adjList[u].append((v, time))
            adjList[v].append((u, time))
        
        # Track shortest times and counts
        shortest = [float('inf')] * n
        ways = [0] * n
        
        shortest[0] = 0
        ways[0] = 1  # One way to stay at start
        
        heap = [(0, 0)]  # (time, node)
        
        while heap:
            curr_time, curr = heapq.heappop(heap)
            
            # Skip outdated entries
            if curr_time > shortest[curr]:
                continue
            
            for neighbor, time in adjList[curr]:
                new_time = curr_time + time
                
                # Case 1: Found a better path
                if new_time < shortest[neighbor]:
                    shortest[neighbor] = new_time
                    ways[neighbor] = ways[curr]  # Inherit count from current
                    heapq.heappush(heap, (new_time, neighbor))
                
                # Case 2: Found an equal path (another way!)
                elif new_time == shortest[neighbor]:
                    ways[neighbor] += ways[curr]
        
        return ways[n - 1] % MOD