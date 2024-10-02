# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return []
        
        else:
            sumArray = []
            depth = 0

            #Traverse the tree adding up the sum and the number of nodes at each level
            def traverse(root, curDepth):
                #print("SumArray: " + str(sumArray))
                if len(sumArray) == curDepth:
                    #print("First value")
                    #Add another array to the first that will hold the sumTotal of all of the nodes at that level and the count of nodes at that level
                    sumArray.append([root.val, 1])

                else:
                    #print("not first node at level")
                    #then update the existing entry in sumArray
                    #print(sumArray[curDepth])
                    sumArray[curDepth][0] += root.val   #update sum total
                    sumArray[curDepth][1] += 1          #update node count

                #Move down the tree
                if root.left != None:
                    traverse(root.left, curDepth + 1)

                if root.right != None:
                    traverse(root.right, curDepth + 1)


            traverse(root, depth)
            #print("The final sumArray: " + str(sumArray))

            #Calculate the average value at each level
            results = []
            for level in sumArray:
                #print(level)
                results.append((level[0] / level[1]))

            #Return the results
            return results