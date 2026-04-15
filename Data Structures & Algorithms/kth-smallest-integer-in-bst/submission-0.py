# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorder(self, root: Optional[TreeNode], arr) -> None:
        if root is None:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        self.inorder(root, self.arr)
        return self.arr[k-1]
        