class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n,m=len(spells),len(potions)
        res=[]
        for spell in spells:
            target = math.ceil(success/spell)
            left,right=0,m
            while left<right:
                mid=left+(right-left)//2
                if potions[mid]>=target:
                    right=mid
                else:
                    left=mid+1
            res.append(m-left)
        return res

        