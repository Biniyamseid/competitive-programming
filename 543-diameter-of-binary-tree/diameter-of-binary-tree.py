# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # mx  = 0
        # def dfs(node):
        #     nonlocal mx
        #     if not node: return 0
        #     left = 1+dfs(node.left)
        #     right = 1+dfs(node.right)
        #     print(left,right,node.val)
        #     mx = max(mx,left+right-2)
        #     return max(left,right)
        # dfs(root)
        # return mx
        mx  = 0
        def dfs(node):
            nonlocal mx
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right) 
            mx = max(mx,left+right)
            return 1+ max(left,right)
        dfs(root)
        return mx
            

        