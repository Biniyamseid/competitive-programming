# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            current_level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                current_level.append(curr.val)
            ans.append(sum(current_level))
        if len(ans) < k :
            return -1
        else: return sorted(ans,reverse=True)[k-1]
            



        