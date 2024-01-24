# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(node,counter):
            if not node:
                return
            if (not node.left) and not (node.right):
                counter[node.val]+=1
                oddcount = 0
                for i in counter:
                    if counter[i]%2:
                        oddcount+=1
                # print(oddcount,counter)
                if oddcount>1:
                    
                    return
                else:
                    ans[0]+=1
                    return
            counter[node.val]+=1
            dfs(node.left,counter.copy())
            dfs(node.right,counter.copy())
           
        dfs(root,defaultdict(int))
        return ans[0]


            
            
        