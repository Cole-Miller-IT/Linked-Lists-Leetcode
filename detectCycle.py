# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while(True):
            if cur == None:
                return False
        
            if cur.val == "@":
                return True
            
            cur.val = "@"
            cur = cur.next
            
            
        return False
        