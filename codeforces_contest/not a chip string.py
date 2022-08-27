from lib2to3.pytree import convert


def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
t = int(input())
for _ in range(t):
    string = input()
    added = []
    lsstring = Convert(string)
    lsstring = sorted(lsstring)
 
    n = int(input())
    count = 0
    ans = ""
    for i in lsstring:
        if count + (int(ord(i)) -int(ord("a"))+1) <= n:
            count += (int(ord(i)) -int(ord("a"))+1)
            added.append(i)
    for i in string:
        if i ==" ":
            ans += " "
            continue
        if i in added:
            ans += i
            added.remove(i)

    print(ans)
    """5
abca
2
abca
6
codeforces
1
codeforces
10
codeforces
100
"""