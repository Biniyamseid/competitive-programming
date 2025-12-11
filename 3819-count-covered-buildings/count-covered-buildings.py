class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xd = defaultdict(list)
        yd = defaultdict(list)

        # group by x and y
        for x, y in buildings:
            xd[x].append((x, y))
            yd[y].append((x, y))

        x_mid = set()
        y_mid = set()

        # buildings with same x (same column)
        for x in xd:
            if len(xd[x]) > 2:
                xd[x].sort(key=lambda p: p[1])       # sort by y
                for i in range(1, len(xd[x]) - 1):
                    x_mid.add(xd[x][i])

        # buildings with same y (same row)
        for y in yd:
            if len(yd[y]) > 2:
                yd[y].sort(key=lambda p: p[0])       # sort by x
                for i in range(1, len(yd[y]) - 1):
                    y_mid.add(yd[y][i])

        # count buildings that are in both middle sets
        count = 0
        for x, y in buildings:
            if (x, y) in x_mid and (x, y) in y_mid:
                count += 1

        return count
