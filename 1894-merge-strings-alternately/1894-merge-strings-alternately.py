class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        for i in range(min(len(word1),len(word2))):
            res=res+word1[i]+word2[i]
        if word1[i+1:]!="":
            res+=word1[i+1:]
        if word2[i+1:]!="":
            res+=word2[i+1:]
        return res
        