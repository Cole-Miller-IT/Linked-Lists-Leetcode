# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #empty tree
        if root == None:
            #print("Empty tree")
            return False

        else: #1 or more nodes
            def traverseTree(root, curSum):
                #print("Current Node: " + str(root.val))

                #Add the node's sum to the current sum
                curSum += root.val
                #print("Current Sum: " + str(root.val))

                #Determine if the current node is a leaf
                if (root.left == None and root.right == None):
                    #leaf
                    #print("leaf")

                    #check if the sum matches the target sum
                    if (curSum == targetSum):
                        return True

                    else:
                        return False

                else: #one or both children exist
                    result = False

                    if (root.left != None):
                        #print("go left")
                        result = traverseTree(root.left, curSum)

                    if (root.right != None and result == False):
                        #print("go right")
                        result = traverseTree(root.right, curSum)

                    return result

            currentSum = 0            
            result = traverseTree(root, currentSum)
            #print(result)
            return result