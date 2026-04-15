# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        dq = deque()

        dq.append(root)
        ans = []

        while(len(dq)):
            ans.append(dq[0].val)
            for i in range(len(dq)):
                el = dq.popleft()
                if el.right:
                    dq.append(el.right)
                if el.left:
                    dq.append(el.left)
        
        return ans



        
        