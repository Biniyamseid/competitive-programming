# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p,q)]
        while queue:
            p,q = queue.pop(0)
            if not p and not q:
                continue
            elif not p or not q:
                return False
            if p.val != q.val:
                return False
            queue.extend([(p.left,q.left),(q.right,p.right)])
        return True
            