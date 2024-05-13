# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Count elements in the list
        length = 0
        node = head
        while node != None:
            length += 1
            node = node.next
            
        #print("list length: " + str(length))
        
        if length == 0:
            return False
        
        if length == 1:
            return True
        
        
        #Determine if the list is even or odd
        odd = True
        if (length % 2) == 0:
            #print("even")
            odd = False
        else:
            #print("odd")
            pass
            
        halfwayLength = int(length / 2)
        #print(halfwayLength)
        
        #Make an array to store the first half of the palindrome
        arrFirstHalf = [None] * halfwayLength #init array of fixed size
        #print(arrFirstHalf)
        
        cur = head
        counter = 1
        index = 0
        searching = True
        while(searching):
            #First Half
            if counter <= halfwayLength:
                #store the elements in reverse order
                arrFirstHalf[(halfwayLength - counter)] = cur.val
                
                cur = cur.next
                counter += 1
                
                #if the palindrome is odd, skip over the middle value
                if counter > halfwayLength and odd == True:
                    cur = cur.next
                
            #Second half
            else:
                #print("------------------------")
                #print("second half")
                #print(arrFirstHalf)
                
                if cur == None:
                    return True
                
                if cur.val != arrFirstHalf[index]:
                    #print("not palindrome " + str(cur.val) + " != " + str(arrFirstHalf[index]))
                    return False

                cur = cur.next
                index += 1
                
                
            
            