class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c=0
        for x in arr:
            c=c+1 if x%2 else 0
            if c==3:
                return True
        return False
        