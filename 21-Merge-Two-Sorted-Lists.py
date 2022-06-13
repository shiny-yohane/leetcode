# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        if not list1 and not list2:
            return None
        
        new_head = ListNode()
        new_curr = new_head
        
        list1_curr = list1
        list2_curr = list2
        
        while list1_curr and list2_curr:
            if list1_curr.val < list2_curr.val:
                new_curr.next = ListNode(list1_curr.val)
                new_curr      = new_curr.next
                list1_curr    = list1_curr.next
            else:
                new_curr.next = ListNode(list2_curr.val)
                new_curr      = new_curr.next
                list2_curr    = list2_curr.next
            
        
        if list1_curr:
            new_curr.next = list1_curr
            
        if list2_curr:
            new_curr.next = list2_curr
        
        return new_head.next
