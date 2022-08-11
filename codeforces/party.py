from collections import defaultdict
def solution():
    t = int(input())
    d = defaultdict(list)
    visited = set()
    maximum = 0
    def dfs(df,count):
        if type(df) == type([]):
            for i in df:
                visited.add(i)
                dfs(i,count+1)
        print(count)
        return count+1

    for t in range(1,t+1):
        num = int(input())
        d[num].append(t)
    maximum = max(maximum,dfs(d[-1],0))
    print(maximum +1)
solution()
    
