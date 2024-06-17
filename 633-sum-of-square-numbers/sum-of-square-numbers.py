class Solution:
    def judgeSquareSum(self, c: int) -> bool:
            # l = 0
            # r = int(c**0.5) + 1  
            # r = c+1
            
            # while l <= r:
            #     res = l**2 + r**2
            #     if res == c:
            #         return True
            #     elif res < c:
            #         l += 1
            #     else:
            #         r -= 1
            
            # return False
        # if c == 0:
        #     return True
        # lst = [i for i in range(1,c)]
        l = 0
        r = int(c**0.5)+1
        while l<=r:
            # res = lst[l]**2 + lst[r]**2
            res = l**2 + r**2
            mid = (l+r)//2
            # print(l,r,mid)
            if res == c:
                return True
            if l**2 + l**2 == c or r**2 +r**2 == c:
                return True
            if mid**2 +mid**2 ==c :
                return True
            if l**2 == c or r**2 == c or mid**2 == c:
                return True
            elif res>c:
                r = r-1
            else:
                l = l+1
        return False



        