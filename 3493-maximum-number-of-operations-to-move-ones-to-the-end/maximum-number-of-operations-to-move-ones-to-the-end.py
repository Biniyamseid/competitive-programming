class Solution:
    def maxOperations(self, s: str) -> int:
        # find how many ones
        # allocate last how many ones position to ones and if they already occupied no problem but if it is not occupied calculate.
        r = 0
        # l = 0 ,if left[l] == "1" find an r for it, replace that place with one and continue for the next 1.

        s_new = s[0]
        for i in range(1,len(s)):
            if s[i]=="0" and s[i-1]=="0":
                continue
            s_new += s[i]
        s= s_new
        count_of_ones = s.count("1")
        left,right = s[0:len(s)-count_of_ones],s[len(s)-count_of_ones:]
        # if right.count("1") == count_of_ones:
        #     return 0
        left = [i for i in left]
        right = [i for i in right]



            
        # print(left,right)
        nl,nr = len(left),len(right)
        counter = 0
        r,l =0,0
        for l in range(len(left)):
            if left[l]=="1":
                while (r in range(len(right))):
                    if right[r]=="0":
                        right[r]="1"
                        # counter += (len(left)-l+r-1)
                        left_walk = nl-l-1
                        right_walk = r+1
                        counter+=left_walk+right_walk
                        # print(right[r])
                        break
                    r+=1
        print(left,right)
        return counter

        