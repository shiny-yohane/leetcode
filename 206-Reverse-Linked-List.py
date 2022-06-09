# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = [] # Space: O(n)
        node = head
        while node: # Time: O(n)
            values.append(node.val)
            node = node.next

        node = head
        while node: # Time: O(n)
            node.val = values.pop()
            node = node.next
        
            
        return head
