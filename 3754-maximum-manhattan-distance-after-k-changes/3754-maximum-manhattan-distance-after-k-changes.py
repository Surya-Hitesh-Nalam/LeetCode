class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x,y=0,0
        maxi=0
        steps=1
        for i in s:
            if i=="N":
                y+=1
            elif i=="S":
                y-=1
            elif i=="E":
                x+=1
            else:
                x-=1
            dis=abs(x)+abs(y)
            maxi=max(maxi,dis,min(steps,dis+(k*2)))
            steps+=1
        return maxi
        