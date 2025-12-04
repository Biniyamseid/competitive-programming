class Solution:
    def countCollisions(self, directions: str) -> int:
        answer = 0
        # RLRLSLL
        # r = 0 start 1
        # l if start and there is active right +2 if s prev +1
        # r continue making active right = 1
        # s and active right+=1 active right = 0
        # l and in any means crash or s happened before and active right not active!=-1 +=1
        stack = []
        # for l in directions:
        #     if l == "R":
        #         stack.append("R")
        #     if l == "L":
        #         if stack and stack[-1] == "R":
        #             stack.pop()
        #             stack.append("S")
        #             answer +=2
        #         elif stack and stack[-1]=="S":
        #             answer+=1
        #         elif stack and stack[-1]=="L":
        #             answer +=0
        #         elif not stack:
        #             stack.append("L")
        #         else:
        #             print('new case')
        #     if l == "S":
        #         if stack and stack[-1]=="R":
        #             answer +=1
        #             stack.pop()
        #             stack.append("S")
        #         else:
        #             stack.append("S")
        # return answer



        # active_right = -1(not right so far),0(s)
        count_r = 0
        active_right = -1
        for l in directions:
            if l =="R":
                active_right = 1
                count_r +=1
            if l == "L":
                if active_right!=-1:
                    if active_right == 1:
                        answer+=2
                        if count_r>1:
                            answer += (count_r-1)
                        active_right = 0
                        count_r = 0
                    elif active_right == 0:
                        answer+=1
                        count_r = 0
                
            if l=="S":
                if active_right == 1:
                    answer+=(count_r)
                    count_r = 0
                active_right = 0
            print(l,answer)
        return answer
        