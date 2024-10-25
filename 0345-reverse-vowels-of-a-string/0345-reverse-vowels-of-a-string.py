class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        v=[]
        res=""
        for i in s:
            if i in vowels:
                v.append(i)
        v.reverse()
        ind=0
        for i in range(len(s)):
            if s[i] in vowels:
                res+=v[ind]
                ind+=1
            else:
                res+=s[i]
        return res

        