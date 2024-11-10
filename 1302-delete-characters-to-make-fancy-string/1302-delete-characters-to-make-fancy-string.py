class Solution:
    def makeFancyString(self, s: str) -> str:
        answer=s[0]
        count=1
        for i in range(1,len(s)):
            if s[i]==answer[-1]:
                count+=1
                if count<3:
                    answer+=s[i]
            else:
                count=1
                answer+=s[i]
        return answer
        