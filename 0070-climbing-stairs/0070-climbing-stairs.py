class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}  
        def backtrack(step):
            if step == n: 
                return 1
            if step > n:  
                return 0
            if step in dp:  
                return dp[step]
            dp[step] = backtrack(step + 1) + backtrack(step + 2)
            return dp[step]
        return backtrack(0)
        