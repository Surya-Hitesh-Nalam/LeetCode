class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqMap = defaultdict(int)
        for c in word:
            freqMap[c]+=1
        frequencies = sorted(freqMap.values())
        mini=float('inf')
        n=len(frequencies)

        for i in range(n):
            base=frequencies[i]
            total_detection=0

            total_detection +=sum(frequencies[:i])
            for j in range(i,n):
                if frequencies[j]>base+k:
                    total_detection+=frequencies[j]-(base+k)
            mini=min(mini,total_detection)
        return mini


        