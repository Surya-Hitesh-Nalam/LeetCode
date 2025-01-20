class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        map={}
        for i in range(m):
            for j in range(n):
                map[mat[i][j]]=[i,j]
        print(map)
        row=[0]*m
        col=[0]*n
        for i in range(len(arr)):
            x=map[arr[i]]
            row[x[0]]+=1
            col[x[1]]+=1
            if row[x[0]]==n or col[x[1]]==m:
                return i
        return -1
        