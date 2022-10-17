class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(":")
        correct = correct.split(":")
        
        cur = 0
        cur2 = 0
        cor2 = 0
        cor = 0
        tot1 = 0
        tot2 = 0
        for i in range(2):
            if i == 0:

                cur += int(current[0][i])*10
                cor += int(correct[0][i])*10
                cur2 += int(current[1][i])*10
                cor2 += int(correct[1][i])*10
            else:
                cur += int(current[0][i])
                cor += int(correct[0][i])
                cur2 += int(current[1][i])
                cor2 += int(correct[1][i]) 
        current_min = cur*60 + cur2
        corr_min = cor*60 +  cor2
        target = abs(current_min-corr_min)
        memo = {}
        print(target)
        
        def backtrack(tar):
            if tar in memo:
                return memo[tar]
            if tar < 0:
                return float("inf")
            if tar == 0:
                return  0
            memo[tar] = min ([1+ backtrack(tar-m) for m in [1,5,15,60]])
            return memo[tar]
        return backtrack(target)        
        