# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Count elements in the list
        counter = 0
        node = head
        while node != None:
            counter += 1
            node = node.next
            
        listLength = counter #5#len(head)
        #print("list length: " + str(listLength))
        
        current = head
        pos = 1 #Start at pos 1/the first element in the list
        stopPos = listLength - n
        #print("Stop Pos: " + str(stopPos))
        
        if stopPos == 0:
            #remove the first element
            head = head.next
            return head
        
        #While the list is not empty
        while listLength > 0:
            #If at the correct spot
            if pos == stopPos:
                #print("at position " + str(pos))
                #print(current)
                
                #Step over the element
                current.next = current.next.next
                #print(current)
                break
                
            else:
                #Take one step forward
                pos += 1
                current = current.next
                
        return head