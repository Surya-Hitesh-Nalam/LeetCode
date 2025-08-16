# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid=self.mid(head)
        left=head
        right=mid.next
        mid.next=None

        left_sorted=self.sortList(left)
        right_sorted=self.sortList(right)
        return self.merge_sort(left_sorted,right_sorted)
    def mid(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge_sort(self,left,right):
        dummy=ListNode(0)
        curr=dummy

        while left and right:
            if left.val<=right.val:
                curr.next=left
                left=left.next
            else:
                curr.next=right
                right=right.next
            curr=curr.next
        curr.next=left if left else right
        return dummy.next

        