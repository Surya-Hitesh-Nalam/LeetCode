class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        for i in range(len(nums)):
            sum1=sum(nums[:i])
            sum2=sum(nums[i+1:])
            if sum1==sum2:
                return i
        else:
            return -1
        