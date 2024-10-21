import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)  # Convert the list into a heap
        count = 0
        
        for _ in range(k):
            # Extract the largest element (inverted back to positive)
            maxi = -heapq.heappop(nums)
            count += maxi
            
            # Push the ceiling of the division by 3 back into the heap
            heapq.heappush(nums, -math.ceil(maxi / 3))
        
        return count


        