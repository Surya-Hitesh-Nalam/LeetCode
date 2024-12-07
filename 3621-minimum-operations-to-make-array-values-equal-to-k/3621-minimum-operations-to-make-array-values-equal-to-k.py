class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=set()
        for i in nums:
            if i<k:
                return -1
            else:
                if i in s :
                    continue
                elif i==k:
                    continue
                else:
                    s.add(i)
        return len(s)
        