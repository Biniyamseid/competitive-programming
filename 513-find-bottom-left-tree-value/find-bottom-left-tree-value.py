# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0
        ans = root.val
        def dfs(node,depth):
            nonlocal maxdepth
            nonlocal ans
            if not node:
                return
            if node.right and depth>maxdepth:
                ans = node.right.val
            if node.left and depth>maxdepth:
                ans = node.left.val
            if node and depth>maxdepth:
                ans = node.val
            maxdepth = max(depth,maxdepth)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
            
        dfs(root,1)
        return ans
            
        