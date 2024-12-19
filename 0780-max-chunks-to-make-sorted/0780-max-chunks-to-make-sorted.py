class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxi=arr[0]
        c=0

        for i in range(len(arr)):
            if maxi<arr[i]:
                maxi=arr[i]
            if maxi==i:
                c+=1
        return c
        

        