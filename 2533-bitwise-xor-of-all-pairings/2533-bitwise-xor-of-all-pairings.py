class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1=0
        xor2=0
        m,n=len(nums1),len(nums2)
        if n%2!=0:
            for i in nums1:
                xor1^=i
        if m%2!=0:
            for i in nums2:
                xor2^=i
        return xor1^xor2
                
        