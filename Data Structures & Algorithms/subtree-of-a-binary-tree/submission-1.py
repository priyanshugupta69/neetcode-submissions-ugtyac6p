# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEqual(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is None:
            return False
        if root2 is not None and root1 is None:
            return False
        
        isLeft = self.isEqual(root1.left, root2.left)
        isRight = self.isEqual(root1.right, root2.right)

        return isLeft and isRight and root1.val == root2.val

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        equalNodes = []

        dq = deque()

        dq.append(root)

        while(len(dq)):
            ele = dq.pop()
            if ele.val == subRoot.val:
                equalNodes.append(ele)
            
            if ele.left:
                dq.append(ele.left)
            if ele.right:
                dq.append(ele.right)

        for node in equalNodes:
            if self.isEqual(node, subRoot) == True:
                return True
        
        return False

        


        