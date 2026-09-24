# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.isMirror(root.left,root.right) if root else True
        
    def isMirror(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isMirror(p.left,q.right)and self.isMirror(p.right,q.left)