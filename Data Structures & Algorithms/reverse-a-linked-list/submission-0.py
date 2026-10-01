# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # current points to first node in a list
        prev = None # 

        while curr:  # while current points at a valid node
             temp = curr.next # keep the continued position before we reverse it
             curr.next = prev # reverse the list
             prev = curr
             curr = temp
        
        return prev
        

        