from itertools import combinations
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        maxC="a"
        startInd=[]
        for i,c in enumerate(word):
            if c>maxC:
                startInd=[]
                maxC=c
            if c==maxC:
                startInd.append(i)
        ans=""
        for i in startInd:
            endInd=len(word)-(numFriends-1-i)
            ans=max(ans,word[i:endInd])
        return ans
        
        
        