# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def sol(self, root: TreeNode, maxi):
        if root is None:
            return 0

        maxi = max(root.val, maxi)
        
        left = self.sol(root.left, maxi)
        right = self.sol(root.right, maxi)

        if root.val >= maxi:
            return 1 + left + right
        
        else:
            return left + right


    def goodNodes(self, root: TreeNode) -> int:
        return self.sol(root, -math.inf )
        