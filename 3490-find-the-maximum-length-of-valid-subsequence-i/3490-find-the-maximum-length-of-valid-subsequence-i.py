class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_c,even_c,odd_ans,even_ans=0,0,0,0
        for num in nums:
            if num%2==0:
                even_c+=1
                even_ans = max(even_ans,odd_ans+1)
            else:
                odd_c+=1
                odd_ans=max(odd_ans,even_ans+1)
        return max(odd_c,even_c,odd_ans,even_ans)


        