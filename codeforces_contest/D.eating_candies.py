def solution():
    t = int(input())
    for _ in range(t):
            n = int(input())
            arr = list(map(int,input().split()))
            if not arr:
                print(0)
                continue
            left_count = 0
            right_count = 0
            l = 0
            total = 0
            r = len(arr) -1
            res = []
            leftarray= []
            rightarray = []
            right,left  = False, False
            while l < r:
                left_count += arr[l]
                right_count += arr[r]
                leftarray.append(arr[l])
                rightarray.append(arr[r])
                total = len(leftarray) + len(rightarray)
                if left_count == right_count:
                    res.append(total)
                else:
                    if l < r-1 and not right and left_count == right_count+arr[r-1]:
                        value = arr[r-1]
                        r = r-1
                        total += 1
                        rightarray.append(value)
                        right_count += value
                        res.append(total)
                        left= False
                        right = True
                    elif  r> l+1 and not left and left_count+arr[l+1] == right_count:
                        value = arr[l+1]
                        l= l+1
                        total += 1
                        leftarray.append(arr[l])
                        res.append(total)
                        left= True
                        right = False
                r-=1
                l+=1

            
            if res:
                last = len(res) -1
                print(res[last])
            else:
                print(0)
solution()



