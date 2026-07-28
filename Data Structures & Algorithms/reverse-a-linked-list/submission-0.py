# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        if not head.next:
            return head
        
        prev_node = None
        current_node = head

        while current_node.next is not None:
            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node
        
        current_node.next = prev_node
        return current_node