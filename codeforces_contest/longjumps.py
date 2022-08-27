def longjump():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        nums = list(map(int,input().split()))
        maxim= 0
        nums = [0] + nums
        for i in range(1,n+1):
            res = i
            ans = 0
            while res < n+1:
                ans += nums[res]
                res += ans
            maxim = max(ans,maxim)
        print(maxim)
longjump()
