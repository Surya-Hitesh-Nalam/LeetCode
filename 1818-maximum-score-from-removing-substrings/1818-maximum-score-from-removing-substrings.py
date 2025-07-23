class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res=0
        if y>x:
            more="ba"
            more_score=y
            least="ab"
            least_score=x
        else:
            more="ab"
            more_score=x
            least="ba"
            least_score=y
        
        l=[]
        for ch in s:
            if ch==more[1] and l and l[-1]==more[0]:
                l.pop()
                res+=more_score
            else:
                l.append(ch)
        
        l2=[]
        for ch in l:
            if ch==least[1] and l2 and l2[-1]==least[0]:
                l2.pop()
                res+=least_score
            else:
                l2.append(ch)
        return res

        