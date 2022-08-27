def ans():
    testcases = int(input())
    for _ in range(testcases):
        n = int(input())
        nums = list(map(int,input().split()))
        maxi = 0
        for i in range(n-1,-1,-1):
            total= 0
            total+=nums[i]
            if (total+i < n):
                total += nums[i+nums[i]]
            nums[i] = total
            maxi = max(maxi,nums[i])
        print(maxi)
ans()