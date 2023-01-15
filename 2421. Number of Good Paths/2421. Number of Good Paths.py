List = list
List = list


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:

        def get_root(i):
            if i == par[i]:
                return i
            par[i] = get_root(par[i])
            return par[i]

        def connect(i, j):
            i, j = get_root(i), get_root(j)

            if i != j:
                if sz[i] < sz[j]:
                    i, j = j, i
                par[j] = i
                sz[i] += sz[j]

                if cur[i] == cur[j]:
                    r = cnt[i] * cnt[j]
                    cnt[i] += cnt[j]
                    return r

                elif cur[i] < cur[j]:
                    cur[i], cnt[i] = cur[j], cnt[j]
            return 0

        n = ans = len(vals)
        sz, cur, cnt,  = [1]*n, vals, [1] * n
        par = list(range(n))
        print(par)

        for a, b in sorted(edges, key=lambda p: max(vals[p[0]], vals[p[1]])):
            ans += connect(a, b)

        return ans


a = Solution()
print(a.numberOfGoodPaths(vals=[1, 3, 2, 1, 3],
      edges=[[0, 1], [0, 2], [2, 3], [2, 4]]))
