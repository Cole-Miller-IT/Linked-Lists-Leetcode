# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Count elements in the list
        counter = 0
        node = head
        while node != None:
            counter += 1
            node = node.next
            
        listLength = counter
        #print("list length: " + str(listLength))
        
        
        if listLength <= 1:
            #print("pass")
            return head
        
        elif listLength == 2:
            #print("swap")
            #swap them around
            nextNode = head.next
            nextNode.next = head
            head.next = None
            head = nextNode
            return head
            
            
        else:   
            #3 or more elements
            #print(">= 3")
            
            prev = head
            current = head.next
            nextNode = head.next.next
            first = True
            while(True):
                #print("")
                #print("prev: " + str(prev))
                #print("cur: " + str(current))
                #print("next: " + str(nextNode))
                
                current.next = prev
                
                if first == True:
                    prev.next = None
                    first = False
                    
                #Move forward a step
                prev = current
                current = nextNode
                if current == None:
                    #Reached the end of the list
                    #print("end")
                    head = prev
                    return head
                
                nextNode = nextNode.next 
                