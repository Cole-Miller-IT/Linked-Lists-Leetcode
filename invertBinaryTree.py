# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        else: #tree exists
            def invertAndTraverse(curNode):
                #Swap/invert Nodes
                curNode.left, curNode.right = curNode.right, curNode.left

                #Repeat for the children
                if curNode.right != None:
                    invertAndTraverse(curNode.right)

                if curNode.left != None:
                    invertAndTraverse(curNode.left)

            invertAndTraverse(root)
            return root
