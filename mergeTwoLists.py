# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #Merges two lists in-place into L1 and returns the merged list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L2 = list2
        L1 = list1
        cur = list1
        
        #Check if lists are empty
        if L1 == None:
            print("L1 empty")
            return L2
        if L2 == None:
            print("L2 empty")
            return L1
        
        head = None
        merging = True
        while(merging):
            print("------------")
            print("Current: " + str(cur))
            print("L2: " + str(L2))
            
            if L2 == None:
                print("L2 empty after merge")
                if head == None:
                    return cur
                else:
                    return head
            
            if L2.val <= cur.val:
                print("L2 goes before L1")
                temp = L2.next
                L2.next = cur
                cur = L2
                L2 = temp
                
            else:
                #No
                #If we have reached the end of L1
                if cur.next == None:
                    print("L1 ended")
                    cur.next = L2
                    if head == None:
                        return cur
                    else:
                        return head
                
                if L2.val <= cur.next.val:
                    #in between
                    print("in between")
                    temp = L2.next
                    L2.next = cur.next
                    cur.next = L2
                    L2 = temp
                    
                else:
                    #No, move cur forwards 1 step
                    if head == None:
                        head = cur
                    
                    print("step forwards")
                    cur = cur.next
            