class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            else:
                return False
        n=len(words)
        count=0
        for i in range(0,n):
            for j in range(0,n):
                if i!=j and i<j:
                    if isPrefixAndSuffix(words[i],words[j]):
                        count+=1
        return count

        