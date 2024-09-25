# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0222.Count%20Complete%20Tree%20Nodes/README_EN.md
#Had to look at some others solutions to understand how to do this in less than O[n] time
#The explanation is on the github too

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            d = 0
            while root:
                d += 1
                root = root.left
            return d

        if root == None:
            return 0

        else:
            leftDepth = depth(root.left)
            rightDepth = depth(root.right)
            
            #If they are equal, then the left subtree is full, record that with bit-shifting then traverse down the right side
            if leftDepth == rightDepth:
                return (1 << leftDepth) + self.countNodes(root.right)

            #If they aren't equal, then the left subtree contains nodes at the lowest depth
            #while the right tree is empty at that depth, record right side with bit-shifting then traverse down the left side
            return (1 << rightDepth) + self.countNodes(root.left)