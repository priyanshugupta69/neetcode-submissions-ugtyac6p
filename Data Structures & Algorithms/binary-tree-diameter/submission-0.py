# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sol(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        sol_left = self.sol(root.left)
        sol_right = self.sol(root.right)
        
        self.maxi = max(self.maxi, (sol_left + sol_right))

        return 1 + max(sol_left, sol_right)
        
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.maxi = 0
        self.sol(root)
        return self.maxi
        