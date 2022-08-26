level = int(input())
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
n1 = l1[0]
n2 = l2[0]
l1 = l1[1:]
l2 = l2[:1]
merged = l1+l2
all_levels = [i for i in range(1,level+1)]
merged_list =sorted(list(set(merged)))
if all_levels == merged_list:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
"""4
3 1 2 3
2 2 4
4
3 1 2 3
2 2 3
4
3 1 2 3
2 2 3"""

