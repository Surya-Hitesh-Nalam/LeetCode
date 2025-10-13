class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[]
        prev=[]
        for i in range(len(words)):
            word=words[i]
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            if count!=prev:
                res.append(word)
                prev=count
        return res
        