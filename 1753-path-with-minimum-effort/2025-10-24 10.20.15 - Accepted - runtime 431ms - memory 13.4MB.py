class Solution(object):
    def minimumEffortPath(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        cells = ROWS * COLS

        efforts = [float('inf')] * cells
        efforts[0] = 0
        heap = [(0, (0, 0))]  # (effort, (row, col))

        while heap:
            curr_effort, pos = heapq.heappop(heap)
            r, c = pos
            curr_idx = r * COLS + c  # ✓ Fixed

            if curr_effort > efforts[curr_idx]:
                continue

            # Early exit optimization
            if r == ROWS - 1 and c == COLS - 1:
                return curr_effort

            curr_height = heights[r][c]

            for dr, dc in [(0,1), (0,-1), (-1,0), (1,0)]:
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    continue

                neighbor_height = heights[nr][nc]
                edge_effort = abs(neighbor_height - curr_height)
                
                # Maximum effort along this path
                new_effort = max(curr_effort, edge_effort)  # ✓ Fixed
                
                neighbor_idx = nr * COLS + nc  # ✓ Fixed

                if new_effort < efforts[neighbor_idx]:
                    efforts[neighbor_idx] = new_effort
                    heapq.heappush(heap, (new_effort, (nr, nc)))  # ✓ Fixed

        return efforts[cells - 1]