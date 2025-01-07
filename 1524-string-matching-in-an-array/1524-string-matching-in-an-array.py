class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr=' '.join(words)
        subStr=[]
        for i in words:
            if arr.count(i)>=2:
                subStr.append(i)
        return subStr
        