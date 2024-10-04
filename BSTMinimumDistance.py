# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        else:
            def in_order_traversal(node):
                if not node:
                    return []
                return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
            
            # Get sorted list of values from in-order traversal
            values = in_order_traversal(root)
            #print(values)

            # Find the minimum difference between consecutive elements
            min_diff = float('inf')
            for i in range(1, len(values)):
                min_diff = min(min_diff, values[i] - values[i - 1])
            
            #print(min_diff)
            return min_diff
