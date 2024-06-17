class Node:
        def __init__(self, val, nextNode):
            self.value = val
            self.nextNode = nextNode
            
            
            
#Implemented as two linked lists. One functions as the normal stack of all of the pushed and popped values. The other (minValueStackTop) maintains the history of the minValues so that pop() remains O(1) time.
class MinStack:
    def __init__(self):
        self.topNode = None
        self.minValue = None
        self.minValueStackTop = None
        

    def push(self, val: int) -> None:
        if self.topNode == None:
            #print("first value")
            newNode = Node(val, None)
            self.topNode = newNode
            
            newNodeTwo = Node(val, None)
            self.minValueStackTop = newNodeTwo
            self.minValue = self.minValueStackTop.value
            
            
        else:
            #print("not first value")
            newNode = Node(val, self.topNode)
            self.topNode = newNode
            
            #Add to the min stack if the value was a minimum value
            if val <= self.getMin():
                newNodeTwo = Node(val, self.minValueStackTop)
                self.minValueStackTop = newNodeTwo
        

    def pop(self) -> None:
        #UPdate the min stack if the popped value was the min value
        if self.topNode.value == self.getMin():
            self.minValueStackTop = self.minValueStackTop.nextNode
            
        self.topNode = self.topNode.nextNode
        

    def top(self) -> int:
        return self.topNode.value
        

    def getMin(self) -> int:
        return self.minValueStackTop.value
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()