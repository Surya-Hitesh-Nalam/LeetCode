class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        dec = [0] * (n + 1)

        for l, r in queries:
            dec[l] += 1
            if r + 1 < len(dec):
                dec[r + 1] -= 1
        print(dec)
        for i in range(1, n):
            dec[i] += dec[i - 1]
        print(dec)
        for i in range(n):
            if dec[i] < nums[i]:
                return False
        return True
        