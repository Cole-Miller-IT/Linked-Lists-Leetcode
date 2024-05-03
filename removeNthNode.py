# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        #print(current)
        
        counter = 0
        node = head
        while node != None:
            counter += 1
            node = node.next
            
        arrLength = counter #5#len(head)
        print("array length: " + str(arrLength))
        
        while arrLength > 0:
            #If at the correct spot
            ######stop at the predessosor, not at the node to remove
            if n == arrLength:
                print("At spot")
                print(current)
                #if we are at the last node
                if current.next == None:
                    print("last")
                    if n == 1:
                        head = None
                    else:
                        current = None
                    
                    
                #at an inside node
                else:
                    print("inside")
                    current.val = current.next.val
                    current.next = current.next.next
                    
                print(current) 
                return head
                
            else:
                #Move forward
                arrLength -= 1
                current = current.next