# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.maxDepths(root)
    def maxDepths(self,root):
        if not root:
            return 0
        ans1 = 1+self.maxDepths(root.left) 
        ans2 = 1+ self.maxDepths(root.right)
        return max(ans1,ans2)
        