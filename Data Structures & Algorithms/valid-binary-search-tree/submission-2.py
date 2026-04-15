# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def sol(self, root, mini, maxi):
        if root is None:
            return True
        left = self.sol(root.left, mini, min(root.val, maxi))
        right = self.sol(root.right, max(root.val, mini), maxi)
        if root.val > mini and root.val < maxi and left and right:
            return True
        else:
            return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.sol(root, -math.inf, math.inf)


        


        