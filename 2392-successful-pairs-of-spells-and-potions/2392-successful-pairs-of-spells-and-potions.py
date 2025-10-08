class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        for s in spells:
            target=math.ceil(success/s)
            l=0
            r=len(potions)
            while l<r:
                mid=l+(r-l)//2
                if potions[mid]>=target:
                    r=mid
                else:
                    l=mid+1
            ans.append(len(potions)-l)
        return ans
        