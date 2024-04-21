class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        if source == destination:
            return True
        for i in range(n):
            graph[i] = []
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        ans = False
        def dfs(node,visited):
            nonlocal ans
            if not graph[node]:
                return 
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    dfs(i,visited)
                visited.add(i)
            if node == destination:
                ans = True
        dfs(source,set())
        return ans

            

        