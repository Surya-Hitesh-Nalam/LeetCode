class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0, 0, 0]
        for item in nums:
            a[item] += 1
        i = 0
        for j in range(len(nums)):
            while ( a[i] == 0 ): i += 1
            nums[j] = i
            a[i] -= 1