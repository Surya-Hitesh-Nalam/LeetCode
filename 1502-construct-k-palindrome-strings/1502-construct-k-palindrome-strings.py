class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        from collections import Counter
        if len(s)<k:
            return False
        c=Counter(s)
        odd_count=sum(freq%2 for freq in c.values())
        return odd_count<=k
        