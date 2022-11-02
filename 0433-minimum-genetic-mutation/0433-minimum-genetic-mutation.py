class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(0,start)])
        visited = set()
        def isneighbour(a,b):
            return sum([1 for i in range(len(a)) if a[i]!= b[i]])
        while queue:
            cost,node = queue.popleft()
            if node == end:
                return cost
            for nei in bank:
                if nei not in visited:
                    if isneighbour(node,nei)==1:
                        visited.add(nei)
                        queue.append((cost+1,nei))
        return -1