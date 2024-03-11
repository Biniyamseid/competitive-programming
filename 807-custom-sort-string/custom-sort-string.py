class Solution:
    def customSortString(self, order: str, s: str) -> str:
        b = list(set([i for i in s]))
        # order = set(order)
        visited = set()
        ans = ""
        count = Counter(s)
        for i in order:
            # if there are duplicates use dictionary
            if i in b:
                ans+=i*count[i]
                # make b a set
                visited.add(i)
                # b.remove(i)
        additional = ""
        for i in s:
            if i not in visited:
                additional+=i
        ans+=additional
        return ans
            

        