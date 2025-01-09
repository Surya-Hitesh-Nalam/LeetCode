class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count=0
        unique=set(s)
        for i in unique:
            start=s.find(i)
            end=s.rfind(i)
            if start<end:
                count+=len(set(s[start+1:end]))
        return count
        