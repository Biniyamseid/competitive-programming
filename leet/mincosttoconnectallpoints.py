from collections import defaultdict
import heapq
from mmap import mmap


def Minc(points):
    n = len(points)
    mmahn = lambda p0,p1 : abs(p0[0] - p1[0]) + abs(p0[1] -p1[1])
    c = defaultdict(list)
    print(n)
    for i in range(n):
        for j in range(i+1,n):
            sums = mmahn(points[i],points[j])
            c[i].append((sums,j))
            c[j].append((sums,i))
    print(c)
Minc([[0,0],[2,2],[3,10],[5,2],[7,0]])
list1 = list((1,2,3,4,5,6,8,5,7,8,9))
print(heapq.heapify(list1))
print(list1)
print(heapq.heappop(list1))

