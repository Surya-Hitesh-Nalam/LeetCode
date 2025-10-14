class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        up=1
        pre_max=0
        res=0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                up+=1
            else:
                pre_max=up
                up=1
            res=max(res,up//2,min(pre_max,up))
        return res>=k
        