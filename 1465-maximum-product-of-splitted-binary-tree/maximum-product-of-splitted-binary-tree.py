# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        ans = 0
        def dfs(node):
            nonlocal total_sum
            if not node:
                return
            total_sum += node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        def dfs2(node,r_sum=0):
            nonlocal total_sum,ans
            if not node:
                return 0
            left = dfs2(node.left)
            right = dfs2(node.right)
            c = node.val+left+right
            ans = max((c*(total_sum-c)),ans)
            # ans = max((total_sum-r_sum)*r_sum,ans)
            # dfs2(node.left,r_sum+node.val)
            # dfs2(node.right,r_sum+node.val)
            return c
        dfs2(root)
        return ans %(10**9 + 7)
            
        