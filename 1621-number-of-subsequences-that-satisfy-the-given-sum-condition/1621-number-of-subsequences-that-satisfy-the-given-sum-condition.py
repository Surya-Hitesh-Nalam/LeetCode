class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        Mod=10**9+7
        nums.sort()
        p=[1]*len(nums)
        for i in range(1,len(nums)):
           p[i]=(p[i-1]*2)%Mod
        
        res=0
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]+nums[r]<=target:
                res=(res+p[r-l])%Mod
                l+=1
            else:
                r-=1
        return res

        