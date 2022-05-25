
def isgood(nums):
    temp =[]
    r = len(nums)
    c = len(nums[0])
    for i in range(1,r):
        m = i-1
        for j in range(1,c):
            n = j-1
            if nums[i][j] < nums[i][n]:
                ans.append([i,j])
                ans.append([m,n])
                return False
    return True
def swap(nums,j,n):
    r = len(nums)
    c = len(nums[0])
    for i in range(r):
        nums[i][j],nums[i][n]=nums[i][n],nums[i][j]
n = int(input())
for i in range(n):
    ans = []
    row,col = input().split()
    print(row,col)
    lst = []
    inp1 = input().split()
    inp2 = input().split()
    inp1 = list(map(int,inp1))
    inp2 = list(map(int,inp2))
    lst.append((inp1))
    lst.append((inp2))
    print(lst)
    print(ans,"ans")
    if isgood(lst):
        print("1","1")
        continue
    elif not isgood(lst):
        print(ans,"ans cr")
        swap(lst,ans[0][1],ans[1][1])
    j,n = ans[0][1],ans[1][1]
    print(j+1,n+1) if isgood(lst) else -1