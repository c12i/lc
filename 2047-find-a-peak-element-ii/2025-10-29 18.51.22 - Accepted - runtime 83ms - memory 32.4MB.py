class Solution(object):
    def findPeakGrid(self, mat):
        m, n = len(mat), len(mat[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        
        # Start from all edges
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m-1 or c == 0 or c == n-1:
                    queue.append((r, c))
                    visited[r][c] = True
        
        while queue:
            r, c = queue.popleft()
            
            # Check if peak
            neighbors = [
                (r-1, c), (r+1, c), (r, c-1), (r, c+1)
            ]
            
            is_peak = True
            for nr, nc in neighbors:
                if 0 <= nr < m and 0 <= nc < n:
                    if mat[nr][nc] > mat[r][c]:
                        is_peak = False
                        if not visited[nr][nc]:
                            queue.append((nr, nc))
                            visited[nr][nc] = True
            
            if is_peak:
                return [r, c]