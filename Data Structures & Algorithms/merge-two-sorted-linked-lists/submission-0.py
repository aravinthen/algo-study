# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        
        node1 = list1
        node2 = list2

        list1_end = False
        list2_end = False

        # create a new list
        merged = ListNode()
        current = merged 

        while not list1_end or not list2_end:
            if node1.val < node2.val:
                current.val = node1.val
                node1 = node1.next

                if node1 is None:
                    list1_end = True
                    break
            else:
                current.val = node2.val
                node2 = node2.next

                if node2 is None:
                    list2_end = True
                    break
            
            next_node = ListNode()
            current.next = next_node
            current = current.next
        
        if not list1_end:
            current.next = node1
        elif not list2_end:
            current.next = node2
        
        return merged 

        