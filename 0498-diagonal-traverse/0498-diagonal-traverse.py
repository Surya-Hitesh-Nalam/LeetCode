class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        row, col = 0, 0
        res = []

        for _ in range(m * n):
            res.append(mat[row][col])

            # Upward direction
            if (row + col) % 2 == 0:
                if col == n - 1:       # If last column → go down
                    row += 1
                elif row == 0:         # If first row → go right
                    col += 1
                else:                  # Normal upward move
                    row -= 1
                    col += 1

            # Downward direction
            else:
                if row == m - 1:       # If last row → go right
                    col += 1
                elif col == 0:         # If first column → go down
                    row += 1
                else:                  # Normal downward move
                    row += 1
                    col -= 1

        return res
