# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return ans
        
        dq = deque()
        dq.append(root)

        while(len(dq)):
            temp = []
            val = []
            while(len(dq)):
                el = dq.popleft()
                temp.append(el)

            for node in temp:
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                val.append(node.val)
                
                
            ans.append(val)

        return ans



        