# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Base Cases
        if p == None and q == None:
            return True

        elif p == None and q != None:
            return False

        elif p != None and q == None:
            return False

        else: #Both of the trees have atleast a root and maybe more nodes below
            pArray = []
            qArray = []

            #Depth-first Search of a binary tree then save the values in an array
            def traverse(root, array):
                #print("At node: " + str(root.val))

                #Add node value to array
                array.append(root.val)

                #Move down to the children
                if root.left != None:
                    #print("At left: " + str(root.left.val))
                    traverse(root.left, array)

                else:
                    array.append(None)

                if root.right != None:
                    #print("At right: " + str(root.right.val))
                    traverse(root.right, array)

                else:
                    array.append(None)

            #print("P traversal")
            traverse(p, pArray)

            #print("Q traversal")
            traverse(q, qArray)

            #Compare the arrays
            #print("p array: " + str(pArray))
            #print("q array: " + str(qArray))
            
            if len(pArray) == len(qArray):
                index = 0
                for element in pArray:
                    #print("Comparing " + str(element) + " and " + str(qArray[index]))
                    if element != qArray[index]:
                        return False

                    index += 1

                return True

            else:
                return False

            