class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        event=[]

        for interval in intervals:
            l,r=interval
            event.append((l,1))
            event.append((r+1,-1))
        event.sort()

        max_group=0
        current_group=0

        for _,eve in event:
            current_group+=eve
            max_group=max(max_group,current_group)
        return max_group
        