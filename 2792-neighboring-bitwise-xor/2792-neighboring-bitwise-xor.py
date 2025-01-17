class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n=len(derived)
        s=0
        for i in derived:
            s^=i
        return s==0
        