class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        start=""
        res=0
        for i in reversed(s):
            start=i+start
            if int(start,2)<=k:
                res+=1
            elif i=='0':
                res+=1
        return res

        