class Solution:
    def maxDiff(self, num: int) -> int:
        mx,my=str(num),str(num)
        j=0
        while mx[j]=='9' and j<len(mx)-1:
            j+=1
        mx=mx.replace(mx[j],'9')

        for i in range(len(my)):
            if i==0:
                if my[i]!="1":
                    my=my.replace(my[i],"1")
                    break
            else:
                if my[i]!='0' and my[i]!=my[0]:
                    my=my.replace(my[i],'0')
                    break
        return int(mx)-int(my)
        