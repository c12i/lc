"""
What we need to keep track of
- minutes elapsed
- number of fresh oranges
- positions of rotten oranges (in a queue)
"""
class Solution(object):
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])

        rq = deque()
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rq.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1

        n = len(rq)
        minutes = 0

        while rq:
            if n == 0:
                minutes += 1
                n = len(rq)

            r, c = rq.popleft()
            n -= 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if (
                    (nr < 0 or nc < 0) or
                    (nr >= ROWS or nc >= COLS) or
                    grid[nr][nc] != 1
                ):
                    continue

                grid[nr][nc] = 2
                num_fresh -= 1
                rq.append((nr, nc))

        return minutes if num_fresh == 0 else -1