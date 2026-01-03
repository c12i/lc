class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        times = [[float('inf')] * COLS for _ in range(ROWS)]
        times[0][0] = 0
        heap = [(0, 0, 0)]  # (time, row, col)
        
        while heap:
            curr_time, r, c = heapq.heappop(heap)
            
            if curr_time > times[r][c]:
                continue
            
            if r == ROWS - 1 and c == COLS - 1:
                return curr_time
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue
                
                # *** move to next cell
                next_time = curr_time + 1
                
                # *** if we arrive too early, calculate wait time
                if grid[nr][nc] > next_time:
                    # Calculate the difference
                    diff = grid[nr][nc] - curr_time
                    # Adjust based on parity
                    if diff % 2 == 0:
                        next_time = grid[nr][nc] + 1
                    else:
                        next_time = grid[nr][nc]
                
                if next_time < times[nr][nc]:
                    times[nr][nc] = next_time
                    heapq.heappush(heap, (next_time, nr, nc))
        
        return -1