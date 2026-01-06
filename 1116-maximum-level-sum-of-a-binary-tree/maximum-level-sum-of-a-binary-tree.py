# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        answer = 1
        max_sum = root.val
        levelmap = {}
        queue = deque([root])
        level = 0
        
        while queue:
            level_sum = 0
            level+=1
            levelsize = len(queue)
            for i in range(levelsize):
                node = queue.popleft()
                level_sum+=node.val
                if node and node.left: queue.append(node.left)
                if node and node.right:queue.append(node.right)
            if level_sum>max_sum:
                max_sum = level_sum
                answer = level
        return answer


        


        