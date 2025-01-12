class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res=[]
        m,n=len(grid),len(grid[0])
        skip=0
        for i in range(m):
            if i%2==0:
                for j in range(n):
                    if not skip:
                        res.append(grid[i][j])
                    skip=not skip
            else:
                for j in range(n-1,-1,-1):
                    if not skip:
                        res.append(grid[i][j])
                    skip=not skip
        return res