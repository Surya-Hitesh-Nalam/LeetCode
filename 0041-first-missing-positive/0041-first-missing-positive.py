class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l=[]
        for n in nums:
            if n>0:
                l.append(n)
        l.sort()
        target=1
        for n in l:
            if n==target:
                target+=1
            elif n>target:
                return target
        return target
        