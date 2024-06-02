"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}
        cloned = Node()
        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            copy = Node(node.val)
            oldtonew[node] = copy
            if not node.neighbors:
                return copy
            for nod in node.neighbors:
                copy.neighbors.append(dfs(nod))
            return copy
        return dfs(node) if node else None 
        