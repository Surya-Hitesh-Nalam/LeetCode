class Solution:
    def kthCharacter(self, k: int) -> str:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        reverse_alpha = "bcdefghijklmnopqrstuvwxyza"
        l = ['a']
        while len(l) < k:
            s = len(l)
            for i in range(s):
                idx = alpha.index(l[i])
                l.append(reverse_alpha[idx])
                if len(l) == k:
                    break        
        return l[k - 1]  
