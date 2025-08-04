class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        fruit_count = defaultdict(int)
        max_len=0
        l=0
        for r in range(n):
            fruit_count[fruits[r]]+=1
            while len(fruit_count)>2:
                fruit_count[fruits[l]]-=1
                if fruit_count[fruits[l]]==0:
                    del fruit_count[fruits[l]]
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len
        