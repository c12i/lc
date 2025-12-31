class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        cells = n * n

        times = [float('inf')] * cells
        times[0] = grid[0][0]  # Start time is the starting cell value
        heap = [(grid[0][0], 0, 0)]  # (time, row, col)
        
        while heap:
            curr_time, r, c = heapq.heappop(heap)
            curr_idx = r * n + c

            if curr_time > times[curr_idx]:
                continue
            
            if r == n - 1 and c == n - 1:
                return curr_time
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                
                # The time needed is the max of current time and the cell value
                new_time = max(curr_time, grid[nr][nc])
                idx = nr * n + nc
                
                if new_time < times[idx]:
                    times[idx] = new_time
                    heapq.heappush(heap, (new_time, nr, nc))
            
        return times[cells - 1]