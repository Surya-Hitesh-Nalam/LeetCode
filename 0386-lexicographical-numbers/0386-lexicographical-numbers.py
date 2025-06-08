class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l=list(map(str,[i for i in range(1,n+1)]))
        l1=sorted(l)
        return list(map(int,l1))
        