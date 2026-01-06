class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == newColor:
            return image

        DIRECTIONS = {
            "up":    (-1,  0),
            "down":  ( 1,  0),
            "left":  ( 0, -1),
            "right": ( 0,  1),
        }

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != originalColor:
                return

            image[r][c] = newColor

            for direction in DIRECTIONS.values():
                dr, dc = direction
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image
