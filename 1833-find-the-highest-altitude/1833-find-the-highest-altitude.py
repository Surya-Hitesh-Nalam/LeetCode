class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude=[]
        altitude.append(0)
        altitude.append(gain[0])
        for i in range(1,len(gain)):
            altitude.append(altitude[-1]+gain[i])
        return max(altitude)
        