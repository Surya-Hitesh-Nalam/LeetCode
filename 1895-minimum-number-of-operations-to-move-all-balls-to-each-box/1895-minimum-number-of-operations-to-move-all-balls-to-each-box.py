class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        onepos=[]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                onepos.append(i)
        print(onepos)
        res=[]
        for i in range(len(boxes)):
            ans=0
            for j in onepos:
                val=abs(j-i)
                ans+=val
            res.append(ans)
        return res 

        